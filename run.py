import subprocess
import sys
import os
import time
import webbrowser
from pathlib import Path

from src.utils.utils import BLUE, RESET
from frontend.scss_watcher import watch_scss

os.environ["PYTHONPATH"] = str(Path(".").resolve())

def main():
    # Paths
    main_path = Path("frontend")
      
    # Iniciar Streamlit
    print(f"\n{BLUE}🃏 Iniciando aplicación Streamlit...{RESET}\n")
    frontend_process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", str(main_path / "app.py"), "--server.runOnSave=False"],  
        cwd="."  
    )
    
    # Abrir el navegador
    webbrowser.open("http://localhost:8501")

    # Configuración de rutas
    SCSS_DIRECTORY = "frontend/static/scss"  # Directorio SCSS
    CSS_DIRECTORY = "frontend/static/css"    # Directorio CSS

    watch_scss(SCSS_DIRECTORY, CSS_DIRECTORY) 


if __name__ == "__main__":
    main()