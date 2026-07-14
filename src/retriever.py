from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore


class Retriever:
    """
    Retrieves the most relevant document chunks for a query.
    """

    def __init__(self):

        self.embedder = EmbeddingModel()

        self.vector_store = VectorStore()

        self.vector_store.load_index()

    def retrieve(self, query, k=5):

        query_embedding = self.embedder.embed_query(query)

        results = self.vector_store.search(
            query_embedding,
            k=k
        )

        return results