import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sass
from src.utils.utils import PURPLE, GRAY, DARK_GRAY, BLUE, RESET

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format=f'{PURPLE}%(levelname)s - {DARK_GRAY}%(message)s{RESET}'
)

class SCSSWatcher(FileSystemEventHandler):
    """
    Observador de cambios en archivos SCSS para recompilación automática.
    """
    def __init__(self, scss_dir, css_dir):
        self.scss_dir = scss_dir
        self.css_dir = css_dir

    def on_modified(self, event):
        if event.src_path.endswith('.scss'):
            logging.info(f"Detected change in {event.src_path}. Recompiling SCSS...")
            self.compile_scss()

    def compile_scss(self):
        try:
            sass.compile(dirname=(self.scss_dir, self.css_dir), output_style='compressed')
            logging.info("SCSS compiled successfully!")
        except sass.CompileError as e:
            logging.error(f"SCSS Compilation Error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error during SCSS compilation: {e}")

def watch_scss(scss_dir, css_dir):
    """
    Función principal para observar cambios en un directorio SCSS.
    """
    if not os.path.exists(scss_dir):
        logging.error(f"SCSS directory '{scss_dir}' does not exist.")
        return
    if not os.path.exists(css_dir):
        os.makedirs(css_dir)
        logging.info(f"CSS directory '{css_dir}' created.")

    event_handler = SCSSWatcher(scss_dir, css_dir)
    observer = Observer()
    observer.schedule(event_handler, path=scss_dir, recursive=True)
    observer.start()
    logging.info(f"Watching '{scss_dir}' for changes...")

    try:
        while True:
            pass  # Mantén el script corriendo
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Stopped watching SCSS directory.")
    observer.join()

if __name__ == "__main__":
    # Configuración de rutas
    SCSS_DIRECTORY = "frontend/static/scss"  # Directorio SCSS
    CSS_DIRECTORY = "frontend/static/css"    # Directorio CSS

    watch_scss(SCSS_DIRECTORY, CSS_DIRECTORY)
