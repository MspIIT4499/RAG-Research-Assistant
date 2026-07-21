from src.embeddings import EmbeddingModel


class Retriever:
    """
    Retrieves the most relevant document chunks for a query.
    """

    def __init__(self, vector_store, embedder=None):

        self.vector_store = vector_store

        if embedder is None:
            self.embedder = EmbeddingModel()
        else:
            self.embedder = embedder

    def retrieve(self, query, k=5):

        query_embedding = self.embedder.embed_query(query)

        return self.vector_store.search(
            query_embedding,
            k=k
        )