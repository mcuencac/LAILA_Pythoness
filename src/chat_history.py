import streamlit as st
import base64
from src.utils.utils import get_env_key, THINKING, BRIGHT_GREEN, TURQUOISE, PASTEL_YELLOW, SPARKLES, RESET, RED, RAISED_HAND



class ChatHistory:
    """Clase para manejar el histórico de mensajes."""
    def __init__(self):
        # Cargar y convertir imagen local
        with open("frontend/static/img/laila_avatar.webp", "rb") as image_laila:
            self.laila_avatar = f"data:image/png;base64,{base64.b64encode(image_laila.read()).decode()}"
        with open("frontend/static/img/user.png", "rb") as image_user:
            self.user_avatar = f"data:image/png;base64,{base64.b64encode(image_user.read()).decode()}"
        self.avatar = self.laila_avatar

        if "messages" not in st.session_state:
            st.session_state.messages = []

    def add_message(self, role, content, hidden=False):
        """Añade un mensaje al historial."""
        st.session_state.messages.append({"role": role, "content": content, "hidden": hidden})

    def get_messages(self):
        """Obtiene todos los mensajes, eliminando la propiedad `hidden`."""
        return [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages]

    def get_visible_messages(self):
        """Obtiene solo los mensajes que no están ocultos."""
        return [msg for msg in st.session_state.messages if not msg.get("hidden", False)]

    def display_message(self, message):
        """Muestra un único mensaje."""
        # print(f"{PASTEL_YELLOW}🔮 Mensaje de: {RESET}{message["role"]}\n {PASTEL_YELLOW}")
        
        if message["role"] == "user":
            self.avatar = self.user_avatar
        else:
            self.avatar = self.laila_avatar

        with st.chat_message(message["role"],avatar=self.avatar):
            st.markdown(message["content"])

    def display_messages(self):
        """Muestra solo los mensajes visibles del historial."""
        for message in self.get_visible_messages():
            self.display_message(message)