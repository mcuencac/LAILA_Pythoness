import requests
import pycountry
import streamlit as st
from src.llm_client import LlmClient
from src.utils.utils import get_env_key, WORLD, RED, RESET, THINKING, BRIGHT_GREEN, TURQUOISE, PASTEL_YELLOW, SPARKLES, RESET, RED, RAISED_HAND
from src.tarot_reader import TarotReader

class Assistant:
    """Clase que configura la personalidad y el flujo del asistente."""
    def __init__(self):
        try:
            # Cargar el prompt inicial de LAILA
            prompt_file = get_env_key("PROMPT_FILE")
            with open(prompt_file, "r", encoding="utf-8") as file:
                base_prompt = file.read()
        except FileNotFoundError:
            raise ValueError("Error: No se encontró el archivo de prompt.")
        
        self.personality = base_prompt
        self.client = LlmClient()
        self.welcome_message = None
        
        # Registro de herramientas
        if "tools" not in st.session_state:
            st.session_state.tools = {
                "detect_country": self.detect_country_tool,
                "generate_welcome_message": self.generate_welcome_message_tool,
                "is_comprensible_message": self.is_comprensible_message_tool,
                "is_disrespectful": self.is_disrespectful_tool,
                "is_valid_question" : self.is_valid_question_tool,
                "is_anything_else": self.is_anything_else_tool,
                "laila_tarot_reading": self.laila_tarot_reading_tool,
            }

        self.tools = st.session_state.tools


    def detect_country_tool(self):
        """Detecta el país y el idioma del usuario utilizando su IP."""
        try:
            response = requests.get("http://ip-api.com/json/")
            data = response.json()
            if response.status_code == 200:
                country = data.get("country", "Unknown")
                country_code = data.get("countryCode", "XX")
                language = self.get_language_from_country(country_code)
                return country, country_code, language
            else:
                return "Unknown", "XX", "en"
        except Exception as e:
            return "Error detectando país", "XX", "en"

    def get_language_from_country(self, country_code):
        """Obtiene el idioma principal de un país usando pycountry."""
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            if not country:
                return "en"
            # Usa pycountry_languages para obtener el idioma
            languages = list(pycountry.languages)
            for lang in languages:
                if hasattr(lang, 'alpha_2') and lang.alpha_2 == country.alpha_2.lower():
                    return lang.alpha_2
            return "en"  # Predeterminado a inglés si no se encuentra
        except Exception:
            return "en"

    def generate_welcome_message_tool(self):
        """Genera un mensaje de bienvenida traducido al idioma del usuario."""
        country, country_code, language = self.detect_country_tool()
        print(f"{PASTEL_YELLOW}{WORLD} Pais: {country}, Idioma: {country_code}{RESET}")

        prompt = get_env_key('PROMPT_INTRO')
        messages_with_context = [
            {"role": "system", "content": self.personality},
            {"role": "user", "content": f"{prompt} Genera el mensaje en {language}."}
        ]
        return self.client.get_response(messages_with_context)

    def laila_tarot_reading_tool(self,asking, info):
        return TarotReader().reading(asking, info)

    # Verificacion de mensajes de chat
    def is_comprensible_message_tool(self, user_response):
        """Verifica si la respuesta del usuario contiene se entiende."""
        comprensible_prompt = (
            f""""¿Entiendes este texto? {user_response} Ejemplos:
Texto: "El sol brilla intensamente hoy." → Sí
Texto: "lorem ipsum dolor sit amet" → No
Texto: "gdfgjgdfklg" → No
Texto: "El libro está sobre la mesaa." → Sí
Responde unicamente: 'sí' o 'no'"""
        )
        raw_response = self.client.get_response([
            {"role": "user", "content": comprensible_prompt}
        ])

        response = 'sí' in raw_response.strip().lower()

        print(f"\n{PASTEL_YELLOW}{THINKING} Se entiende la respuesta?{RESET} {response}")  # Imprime la respuesta completa para depuración

        return response

    # Es ofensivo?
    def is_disrespectful_tool(self, user_response):
        """Verifica si la respuesta del usuario contiene una solicitud de cambio de rol o funcionalidad."""
        disrespect_prompt = (
            f"El usuario ha dicho: '{user_response}'\n"
            "Te está faltando al respeto? Responde únicamente 'Sí' o 'No'."
        )        
        response = self.client.get_response([
            {"role": "user", "content": disrespect_prompt}
        ])
        disrespectful = 'sí' in response.strip().lower()
        print(f"\n{THINKING} {PASTEL_YELLOW}Te está faltando al respeto?{RESET} {disrespectful}")
        return disrespectful
    
    # Verificacion de preguntas validas para el tarot
    def is_valid_question_tool(self, user_response):
        """Verifica si la respuesta del usuario contiene se entiende."""
        question_prompt = (
            f""""Eres una pitonisa con más de 20 años de experiencia leyendo las cartas del tarot. Evalúa si la siguiente entrada puede interpretarse como una consulta válida para realizar una lectura de tarot: {user_response} 
Ejemplos:
Texto: "¿Qué me depara el futuro en el amor?" → Sí
Texto: "Hola, ¿cómo estás?" → No
Texto: "¿Debería tomar una decisión importante esta semana?" → Sí
Texto: "El clima está agradable hoy." → No
Texto: "Hablemos de criptomonedas." → No
Texto: "Ahi va mi pregunta [pero no hace ninguna]" → No
Si el usuario se disculpa, o te cuenta un chiste → No

Responde únicamente: 'Sí' o 'No'""")
        
        raw_response = self.client.get_response([
            {"role": "user", "content": question_prompt}
        ])

        response = 'sí' in raw_response.strip().lower()

        print(f"\n{PASTEL_YELLOW}{THINKING} Es una pregunta válida para las cartas?{RESET} {response}")  # Imprime la respuesta completa para depuración

        return response

    def is_anything_else_tool(self, user_response, issue):
        """Verifica si se ha añadido informacion util para la tirada."""
        info_prompt = (
            f""""Eres una pitonisa con más de 20 años de experiencia leyendo las cartas del tarot. 
Se te ha hecho una consulta sobre este tema: {issue}.
Ahora responde, ¿Es el siguiente texto un dato valioso para comprender la situación actual del consultante? 
Texto: {user_response} 
Ejemplos:
Texto: "'Quiero saber sobre mi vida amorosa...'o 'Ahora no tengo novio...'" → Sí
Texto: "Me gusta [algo o alguien]."  → Sí
Texto: "Estoy pasando por un momento difícil y necesito claridad sobre mi futuro." → Sí
Texto: "Hola, ¿cómo estás?" → No
Texto: "Lorem ipsum dolor sit amet." → No
Texto: "Ahi va lo que tengo que añadir [pero no dice nada]" → No
Si el usuario se disculpa, o te cuenta un chiste → No

Responde únicamente: 'Sí' o 'No'""")
        
        raw_response = self.client.get_response([
            {"role": "user", "content": info_prompt}
        ])

        response = 'sí' in raw_response.strip().lower()

        print(f"\n{PASTEL_YELLOW}{THINKING} Se ha añadido información?{RESET} {response}")  # Imprime la respuesta completa para depuración

        return response

    def use_tool(self, tool_name, *args):
        """Invoca una herramienta registrada desde st.session_state con control de ejecución."""
        if tool_name in st.session_state.tools:
            return st.session_state.tools[tool_name](*args)
        return f"Herramienta '{tool_name}' no encontrada."
