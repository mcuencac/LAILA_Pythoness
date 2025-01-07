from dotenv import load_dotenv
from pathlib import Path
import os
import streamlit as st

# Definición de colores e iconos
# Definición de colores e iconos

TURQUOISE = "\033[38;5;87m"
PASTEL_YELLOW = "\033[38;5;187m"
RED = "\033[31m"
BLUE = "\033[34m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"
BRIGHT_RED = "\033[91m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLACK = "\033[90m"
PURPLE = "\033[35m"
GRAY = "\033[37m"
DARK_GRAY = "\033[90m"
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
RESET = "\033[0m"

EYES = "\U0001F440"          # 👀
SPARKLES = "\U00002728"      # ✨
PAGE = "\U0001F5D2"          # 🗒️
GREEN_CIRCLE = "\U0001F7E2"  # 🟢
RED_CIRCLE = "\U0001F534"    # 🔴
CROSS_MARK = "\U0000274C"    # ❌
STAR = "\U00002B50"          # ⭐
WORLD = "\U0001F30D"         # 🌍 
CELEBRATION = "\U0001F389"   # 🎉
THINKING = "\U0001F914"      # 🤔
RAISED_HAND = "\U0000270B"   # ✋

def get_env_key(env_key, levels_up=2, env_file_name=".env"):
    """
    Obtiene una clave específica de un archivo .env ubicado en un nivel superior.

    Parameters:
    - env_key (str): El nombre de la clave que se quiere recuperar.
    - levels_up (int): Cuántos niveles hacia arriba buscar el archivo .env (por defecto, 2).
    - env_file_name (str): El nombre del archivo .env (por defecto, ".env").

    Returns:
    - str: El valor de la clave solicitada.
    """
    try:
        # Resolver la ruta al archivo .env
        dotenv_path = Path(__file__).resolve().parents[levels_up] / env_file_name
        if not dotenv_path.exists():
            message = f"{RED}{CROSS_MARK} Error: FileNotFoundError: No se encontró el archivo .env en {dotenv_path}{RESET}"
            print(message)
            raise FileNotFoundError(message)

        # Cargar las variables del archivo .env
        load_dotenv(dotenv_path=dotenv_path)

        # Obtener la clave API
        key = os.environ.get(env_key)
        if key is None:
            message = f"{RED}{CROSS_MARK} Error: ValueError: La clave '{env_key}' no está configurada en el archivo .env.{RESET}"
            print(message)
            raise ValueError(message)

        return key

    except (FileNotFoundError, ValueError):
        # El mensaje ya se imprime dentro de los bloques anteriores
        raise

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'''
                <head>
                    <!-- Material Icons -->
                    <link href="{url}" rel="stylesheet">
                </head>
                ''', unsafe_allow_html=True)   
    
def svg_write():
        # Write the HTML
        svg_code = ''' _ '''