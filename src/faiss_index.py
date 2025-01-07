import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np
from charset_normalizer import detect
from nltk.tokenize import sent_tokenize

class FaissIndex:
    def __init__(self, model_name='all-MiniLM-L6-v2', data_dir="context", index_file="data/faiss_index.pkl", fragment_size=1000):
        self.model = SentenceTransformer(model_name)
        self.data_dir = data_dir
        self.index_file = index_file
        self.index = None
        self.docs = []
        self.fragment_size = fragment_size
        self.load_or_create_index()

    def detect_encoding(self, file_path):
        """Detecta automáticamente la codificación del archivo."""
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            result = detect(raw_data)
            return result['encoding']

    def split_into_fragments(self, text):
        """
        Divide un texto en fragmentos más pequeños de tamaño definido.
        Utiliza sent_tokenize para mantener la coherencia entre oraciones.
        """
        sentences = sent_tokenize(text)
        fragments = []
        current_fragment = ""
        for sentence in sentences:
            if len(current_fragment) + len(sentence) <= self.fragment_size:
                current_fragment += sentence + " "
            else:
                fragments.append(current_fragment.strip())
                current_fragment = sentence + " "
        if current_fragment:
            fragments.append(current_fragment.strip())
        return fragments

    def create_index(self):
        """Crea un índice FAISS a partir de documentos en el directorio."""
        embeddings = []
        for file_name in os.listdir(self.data_dir):
            file_path = os.path.join(self.data_dir, file_name)
            try:
                encoding = self.detect_encoding(file_path)
                with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                    content = f.read()
                    fragments = self.split_into_fragments(content)
                    for fragment in fragments:
                        self.docs.append(fragment)
                        embeddings.append(self.model.encode(fragment))
            except Exception as e:
                print(f"Error al procesar el archivo {file_name}: {e}")

        if not embeddings:
            raise ValueError("No se generaron embeddings. Verifica tus documentos.")

        embeddings = np.array(embeddings)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

        with open(self.index_file, 'wb') as f:
            pickle.dump((self.index, self.docs), f)
        print(f"Índice FAISS creado y guardado en {self.index_file}")

    def load_index(self):
        """Carga un índice FAISS desde un archivo, con verificación de errores."""
        try:
            with open(self.index_file, 'rb') as f:
                self.index, self.docs = pickle.load(f)
            print(f"Índice FAISS cargado correctamente desde {self.index_file}")
        except (FileNotFoundError, pickle.UnpicklingError):
            print("Error al cargar el índice FAISS. Creando uno nuevo...")
            self.create_index()

    def load_or_create_index(self):
        """Carga o crea un índice FAISS al iniciar la aplicación."""
        if os.path.exists(self.index_file):
            self.load_index()
        else:
            print("El archivo de índice no existe. Creando un nuevo índice FAISS...")
            self.create_index()

    def search(self, query, top_k=3, max_characters=2000):
        """Busca en el índice FAISS usando un query y limita la longitud total de los resultados."""
        if not self.index:
            raise ValueError("El índice no está cargado.")

        query_vector = self.model.encode(query).reshape(1, -1)
        distances, indices = self.index.search(query_vector, top_k)

        relevant_docs = []
        current_length = 0
        for i in indices[0]:
            doc = self.docs[i]
            if current_length + len(doc) <= max_characters:
                relevant_docs.append(doc)
                current_length += len(doc)
            else:
                break

        return relevant_docs

if __name__ == "__main__":
    index = FaissIndex()
    index.load_index()

    # Realizar una búsqueda de prueba
    query = "la emperatriz"
    resultados = index.search(query, top_k=30)
    print("Resultados de la búsqueda:", resultados)
