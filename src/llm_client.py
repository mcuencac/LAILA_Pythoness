from groq import Groq, RateLimitError
from openai import OpenAI
from src.utils.utils import get_env_key, RED, TURQUOISE, RESET

class LlmClient:
    """Clase para manejar la interacción con Groq usando el patrón Singleton."""
    _instance = None  # Implementación de Singleton

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LlmClient, cls).__new__(cls)
            cls._instance._init_instance(*args, **kwargs)  # Corregido: un solo guion bajo
        return cls._instance

    # model = "gpt-3.5-turbo-0125"
    # model = "llama-3.3-70b-versatile"
    # model = "gemma2-9b-it"
    # model = "mixtral-8x7b-32768" # No responde bien... 
    # model = "llama-3.1-8b-instant"
    model = "llama3-8b-8192"
    def _init_instance(self, llm_model=model):  # Corregido a un solo guion bajo
        self.llm_model = llm_model
        print(f"🤖 {TURQUOISE}Iniciando con el LLM: {llm_model}{RESET}\n")

        if self.llm_model.startswith("gpt-"):
            openai_api_key = get_env_key('OPENAI_API_KEY')
            if not openai_api_key:
                raise ValueError("La clave OPENAI_API_KEY no está definida en las variables de entorno.")
            self.client = OpenAI(api_key=openai_api_key)
        else:           
            groq_api_key = get_env_key('GROQ_API_KEY')
            if not groq_api_key:
                raise ValueError("La clave GROQ_API_KEY no está definida en las variables de entorno.")
            self.client = Groq()

    def get_response(self, messages_with_context):
        try:
            response_stream = self.client.chat.completions.create(
                messages=messages_with_context,
                model=self.llm_model,
                temperature=0.2,
                max_tokens=1024,
                top_p=1,
                stream=True
            )

            response_text = ""
            for chunk in response_stream:
                try:
                    content = chunk.choices[0].delta.content
                    if content:  
                        response_text += content
                except (AttributeError, IndexError, KeyError) as e:
                    print(f"Error al procesar chunk: {e}")

            if not response_text:
                raise ValueError("El flujo de respuesta está vacío o no contiene texto válido.")
            return response_text

        except RateLimitError as e:
            try:
                error_code = e.response.json().get('error', {}).get('code', 'unknown_error')
            except AttributeError:
                error_code = 'unknown_error'
            print(f"😿 {RED}Error:{RESET} {e.message}")
            return f"😿 ¡Ah, las cartas! Misteriosas y caprichosas... algo interfiere en mi sagrada conexión con ellas...\n❌ Error: {error_code} ❌\nLas energías se agitan, y cuando esto sucede, la verdad se oculta tras un manto de sombras. Sin embargo, no temas, pues lo que el tarot guarda, tarde o temprano será revelado. Necesito un momento para purificar la conexión... y entonces, corazón, el mensaje se revelará con la fuerza de lo inevitable."

        except Exception as e:
            print(f"Error inesperado: {e}")
            return "Error inesperado al procesar la solicitud."
