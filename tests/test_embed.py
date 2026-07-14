from src.pdf_loader import PDFLoader
from src.chunker import Chunker
from src.embeddings import EmbeddingModel

loader = PDFLoader()
chunker = Chunker()
embedder = EmbeddingModel()

with open("data/attention.pdf", "rb") as pdf:
    pages = loader.load_pdf(pdf)

chunks = chunker.split_documents(pages)

embeddings = embedder.embed_documents(chunks)

print("=" * 60)
print("Number of Chunks:", len(chunks))
print("Embedding Shape:", embeddings.shape)
print("=" * 60)

query_embedding = embedder.embed_query(
    "What optimizer was used?"
)

print("Query Embedding Shape:", query_embedding.shape)