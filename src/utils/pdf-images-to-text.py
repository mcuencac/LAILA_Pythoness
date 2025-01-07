from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract
import os
from tqdm import tqdm
from utils import BRIGHT_GREEN, TURQUOISE, PASTEL_YELLOW, RESET, STAR, THINKING, CELEBRATION, EYES, PAGE
from ocr_processor import OCRProcessor  # Importar la clase OCRProcessor
import warnings
warnings.filterwarnings("ignore") # TODO eliminar warnings

# Configurar la ruta de Tesseract si es necesario
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\\Program Files\\Tesseract-OCR\\tessdata'

def extraer_texto_y_ocr_de_pdf(pdf_path, output_path, password=None):
    """
    Extrae texto incrustado y realiza OCR de un archivo PDF,
    combinando ambos resultados en un archivo de texto.
    """
    # Crear un lector para el PDF
    reader = PdfReader(pdf_path)

    print(f"\n{BRIGHT_GREEN}{THINKING} Leyendo documento...{RESET}\n")
    # Verificar si el PDF está cifrado
    if reader.is_encrypted:
        print(f"{PASTEL_YELLOW}El archivo PDF está cifrado. Intentando descifrar...{RESET}")
        if password:
            # Intentar descifrar con la contraseña proporcionada
            try:
                reader.decrypt(password)
                print(f"{BRIGHT_GREEN}PDF descifrado correctamente.{RESET}")
            except Exception as e:
                print(f"{BRIGHT_GREEN}Error al descifrar el PDF: {e}{RESET}")
                return
        else:
            print(f"{BRIGHT_GREEN}No se proporcionó una contraseña para descifrar el PDF.{RESET}")
            return

    # Convertir las páginas del PDF en imágenes para OCR
    images = convert_from_path(pdf_path)

    # Instanciar el procesador OCR
    ocr_processor = OCRProcessor(device="cpu")

    # Preparar archivo de salida
    with open(output_path, "w", encoding="utf-8") as output_file:
        # Barra de progreso para todas las páginas
        with tqdm(total=len(images), desc=f"{PASTEL_YELLOW}{PAGE}  Procesando páginas{RESET}", unit="pagina") as progress_bar:
            for i, (page, image) in enumerate(zip(reader.pages, images), start=1):
                try:
                    # Extraer texto incrustado
                    embedded_text = page.extract_text() or ""

                    # Guardar la imagen como archivo temporal para OCRProcessor
                    temp_image_path = f"temp_page_{i}.jpg"
                    image.save(temp_image_path)

                    # Extraer texto con OCRProcessor
                    ocr_text = ocr_processor.process_image(temp_image_path)

                    # Eliminar archivo temporal
                    os.remove(temp_image_path)

                    # Combinar los resultados
                    combined_text = f"{embedded_text}\n{ocr_text}\n"
                    
                    #TODO corregir texto con LLM

                    # Escribir en el archivo de salida
                    output_file.write(combined_text)
                except Exception as e:
                    print(f"Error procesando la página {i}: {e}")
                
                # Actualizar la barra de progreso
                progress_bar.update(1)

    return output_path

if __name__ == "__main__":
    # Ruta del archivo PDF original
    pdf_path = "data/el-tarot.pdf"

    # Ruta de salida para el archivo de texto
    output_path = "data/extracted_text_el_tarot.txt"

    # Contraseña del PDF (si está cifrado)
    pdf_password = None  # Proporciona la contraseña si el archivo está protegido

    # Extraer texto y guardar
    result_path = extraer_texto_y_ocr_de_pdf(pdf_path, output_path, password=pdf_password)
    print(f"\n{STAR} {TURQUOISE}Texto extraído con éxito y guardado en:{RESET} {result_path}\n")
    print(f"\n{BRIGHT_GREEN}¡Listo! {CELEBRATION}{RESET}\n")
