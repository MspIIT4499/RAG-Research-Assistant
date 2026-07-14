from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Generates embeddings for document chunks
    using the BAAI embedding model.
    """

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def embed_documents(self, chunks):

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        return embeddings

    def embed_query(self, query):

        return self.model.encode(query)