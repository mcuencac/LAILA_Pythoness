import random
from src.rag import RAG
from src.llm_client import LlmClient
from src.utils.utils import get_env_key, BLUE, PURPLE, RESET, RED, PASTEL_YELLOW

class TarotReader:
    def __init__(self):
        self.rag = RAG()  # Carga el índice una vez al crear la instancia
        self.llm_client = LlmClient(ll_model = "gpt-3.5-turbo-0125")
        # Lista de cartas del Tarot almacenada correctamente como un atributo de la instancia
        self.tarot_cards = [
            "El Loco", "El Mago", "La Sacerdotisa", "La Emperatriz", "El Emperador", 
            "El Hierofante", "Los Enamorados", "El Carro", "La Justicia", "El Ermitaño",
            "La Rueda de la Fortuna", "La Fuerza", "El Colgado", "La Muerte", "La Templanza",
            "El Diablo", "La Torre", "La Estrella", "La Luna", "El Sol", "El Juicio", "El Mundo",
            
            # Arcanos Menores - Bastos (As al Rey)
            "As de Bastos", "Dos de Bastos", "Tres de Bastos", "Cuatro de Bastos", "Cinco de Bastos",
            "Seis de Bastos", "Siete de Bastos", "Ocho de Bastos", "Nueve de Bastos", "Diez de Bastos",
            "Sota de Bastos", "Caballo de Bastos", "Reina de Bastos", "Rey de Bastos",
            
            # Arcanos Menores - Copas (As al Rey)
            "As de Copas", "Dos de Copas", "Tres de Copas", "Cuatro de Copas", "Cinco de Copas",
            "Seis de Copas", "Siete de Copas", "Ocho de Copas", "Nueve de Copas", "Diez de Copas",
            "Sota de Copas", "Caballo de Copas", "Reina de Copas", "Rey de Copas",
            
            # Arcanos Menores - Espadas (As al Rey)
            "As de Espadas", "Dos de Espadas", "Tres de Espadas", "Cuatro de Espadas", "Cinco de Espadas",
            "Seis de Espadas", "Siete de Espadas", "Ocho de Espadas", "Nueve de Espadas", "Diez de Espadas",
            "Sota de Espadas", "Caballo de Espadas", "Reina de Espadas", "Rey de Espadas",
            
            # Arcanos Menores - Oros (As al Rey)
            "As de Oros", "Dos de Oros", "Tres de Oros", "Cuatro de Oros", "Cinco de Oros",
            "Seis de Oros", "Siete de Oros", "Ocho de Oros", "Nueve de Oros", "Diez de Oros",
            "Sota de Oros", "Caballo de Oros", "Reina de Oros", "Rey de Oros"
        ]

    def rag_question(self, question):
        response = self.rag.ask_question(question)
        return response  # Retorna la respuesta correctamente
    
    def get_random_cards(self):
        """
        Genera y devuelve una lista de 6 cartas aleatorias únicas del Tarot.
        """
        # Selecciona 6 números aleatorios entre 0 y 77 (índices de la lista)
        indices = random.sample(range(0, 78), 6)
        cartas_seleccionadas = [self.tarot_cards[i] for i in indices]
        return cartas_seleccionadas

    def reading(self,asking, info):
        """
        Realiza una tirada de Tarot con la pirámide invertida de 6 cartas y genera la interpretación.
        """
        cards = self.get_random_cards()
        # Utilizando un bucle para recopilar la información de todas las cartas
        cards_info = [self.rag_question(f"Dame toda la información sobre la carta {card}") for card in cards]
        # Agregando la explicación de la reading al final
        cards_info.append(self.rag_question("Explícame la reading 'Pirámide Invertida de 6 cartas'"))
        info_cards = "\n".join(cards_info)

        # Interacción con el modelo LLM
        conversation_history = []
        question = f"Se ha hecho una tirada (Piramide invertida de 6 cartas) y han salido en este orden: {cards}. Pregunta: {asking}. Info adicional: {info}. (Realiza la tirada de forma dramática, esotérica y teatral, puedes usar emojis)"
        print(f"\n{PURPLE}Se ha hecho una tirada (Piramide invertida de 6 cartas) y han salido en este orden:\n{RESET}{cards}\n{PURPLE}Pregunta:{RESET} {asking}.\n{PURPLE}Info adicional:{RESET} {info}.")
        conversation_history.append({"role": "system", "content": f"{get_env_key('PROMPT_FILE')}"})
        conversation_history.append({"role": "system", "content": f"## CONTEXTO:\n{info_cards}"})
        conversation_history.append({"role": "user", "content": question})
        response = self.llm_client.get_response(conversation_history)
        return response

if __name__ == "__main__":
    tarot_reader = TarotReader()
    pregunta = "¿Cómo será mi año?"
    info_adicional = "Estoy buscando orientación general para el próximo año."
    resultado = tarot_reader.reading(pregunta, info_adicional)
    print(f"\n{PASTEL_YELLOW}Resultado de la lectura del Tarot:{RESET}\n{resultado}")