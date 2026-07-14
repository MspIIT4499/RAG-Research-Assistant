import faiss
import numpy as np
import pickle


class VectorStore:
    """
    Stores and searches document embeddings using FAISS.
    """

    def __init__(self):

        self.index = None
        self.documents = None

    def create_index(self, embeddings, chunks):

        embeddings = np.array(embeddings).astype("float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        self.documents = chunks

    def save_index(self):

        faiss.write_index(self.index, "vectorstore/faiss.index")

        with open("vectorstore/documents.pkl", "wb") as f:
            pickle.dump(self.documents, f)

    def load_index(self):

        self.index = faiss.read_index("vectorstore/faiss.index")

        with open("vectorstore/documents.pkl", "rb") as f:
            self.documents = pickle.load(f)

    def search(self, query_embedding, k=5):

        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for idx in indices[0]:
            results.append(self.documents[idx])

        return results