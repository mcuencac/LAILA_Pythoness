import torch
from transformers import AutoModel, AutoTokenizer
import warnings
warnings.filterwarnings("ignore") # TODO eliminar warnings


class OCRProcessor:
    def __init__(self, model_name='ucaslcl/GOT-OCR2_0', device="cpu"):
        """
        Inicializa el procesador OCR con el modelo especificado y configura el dispositivo.

        :param model_name: Nombre del modelo preentrenado a cargar.
        :param device: Dispositivo para ejecutar el modelo (por defecto 'cpu').
        """
        self.device = device

        # Cargar el tokenizador y el modelo
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(
            model_name,
            trust_remote_code=True,
            low_cpu_mem_usage=False,
            use_safetensors=True,
            pad_token_id=self.tokenizer.eos_token_id
        ).to(self.device)
        
        self.model = self.model.eval()

        # Asegurar que todos los parámetros del modelo estén en FP32
        for param in self.model.parameters():
            param.data = param.data.float()
            if param.grad is not None:
                param.grad.data = param.grad.data.float()

    def process_image(self, image_path, ocr_type='ocr'):
        """
        Procesa una imagen y extrae texto usando el modelo OCR.

        :param image_path: Ruta al archivo de imagen.
        :param ocr_type: Tipo de OCR (por defecto 'ocr').
        :return: Texto extraído de la imagen.
        """
        try:
            # Tokenizar la imagen
            inputs = self.tokenizer(image_path, return_tensors="pt")
            input_ids = inputs.input_ids.to(self.device).float()
            attention_mask = inputs.attention_mask.to(self.device).float() if 'attention_mask' in inputs else None

            if attention_mask is not None:
                attention_mask = attention_mask.float()

            # Generar resultado
            result = self.model.chat(self.tokenizer, image_path, ocr_type=ocr_type)
            return result

        except Exception as e:
            raise RuntimeError(f"Error durante el procesamiento de la imagen: {e}")

    def save_result(self, text, output_file_path):
        """
        Guarda el texto extraído en un archivo.

        :param text: Texto a guardar.
        :param output_file_path: Ruta al archivo de salida.
        """
        try:
            with open(output_file_path, "w", encoding="utf-8") as file:
                file.write(text)
        except Exception as e:
            raise RuntimeError(f"Error al guardar el archivo: {e}")

# Ejemplo de uso
def main():
    # Crear una instancia del procesador OCR
    ocr = OCRProcessor(model_name='ucaslcl/GOT-OCR2_0', device="cpu")

    # Ruta de la imagen y del archivo de salida
    image_path = "data/pag.jpg"
    output_file_path = "output_text.txt"

    # Procesar la imagen
    try:
        extracted_text = ocr.process_image(image_path)
        print("Texto extraído de la imagen:")
        print(extracted_text)

        # Guardar el resultado
        ocr.save_result(extracted_text, output_file_path)
        print(f"Texto extraído guardado en: {output_file_path}")

    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
