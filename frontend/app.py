import os
import streamlit as st
from src.chat_app import ChatApp
from src.utils.utils import local_css
from PIL import Image
import base64

def main():
        # Cargar configuración y CSS
        local_css(os.path.join(os.path.dirname(__file__), 'static/css', 'styles.css'))

        with st.container(key="header"):
            try:
                # Ruta de la imagen
                image_path = "frontend/static/img/laila_header.png"

                # Verificar si la imagen existe
                if os.path.exists(image_path):
                        # Abrir la imagen y convertirla a Base64
                        with open(image_path, "rb") as laila_header:
                            img_laila_header = f"data:image/png;base64,{base64.b64encode(laila_header.read()).decode()}"

                        # CSS para incluir la imagen de fondo
                        header_bg_img = f"""
                        <style>
                        .stVerticalBlock.st-key-header {{
                            background-image: url("{img_laila_header}");
                        }}
                        </style>
                        """

                        # Insertar en la aplicación                        
                        st.markdown(header_bg_img, unsafe_allow_html=True)
                else:
                    st.error("No se encontró la imagen.")
            except Exception as e:
                st.error(f"Error al cargar la imagen: {e}")

        # Inicializar la aplicación
        app = ChatApp()
        app.run()

if __name__ == "__main__":
    main()