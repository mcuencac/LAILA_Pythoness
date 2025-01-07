import os
from langchain_core.documents import Document
from PyPDF2 import PdfReader

class LocalDocumentClient:
    @staticmethod
    def load_local_documents(directory_path):
        """
        Carga documentos desde una carpeta local y los convierte a objetos Document.
        Soporta archivos .txt y .pdf.
        """
        documents = []
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)

            # Verifica si es un archivo válido
            if os.path.isfile(file_path):
                if file_name.endswith('.txt'):
                    # Procesar archivos de texto
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        documents.append(Document(
                            page_content=content,
                            metadata={"id": file_name, "title": file_name}
                        ))
                elif file_name.endswith('.pdf'):
                    # Procesar archivos PDF
                    content = LocalDocumentClient._extract_text_from_pdf(file_path)
                    documents.append(Document(
                        page_content=content,
                        metadata={"id": file_name, "title": file_name}
                    ))
        return documents

    @staticmethod
    def _extract_text_from_pdf(file_path):
        """
        Extrae texto de un archivo PDF utilizando PyPDF2.
        """
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text.strip()
        except Exception as e:
            print(f"Error al procesar el archivo PDF {file_path}: {e}")
            return ""
