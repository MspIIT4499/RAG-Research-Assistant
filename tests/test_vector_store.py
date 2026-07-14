from src.pdf_loader import PDFLoader
from src.chunker import Chunker
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore

loader = PDFLoader()
chunker = Chunker()
embedder = EmbeddingModel()
vector_store = VectorStore()

with open("data/attention.pdf", "rb") as pdf:
    pages = loader.load_pdf(pdf)

chunks = chunker.split_documents(pages)

embeddings = embedder.embed_documents(chunks)

vector_store.create_index(embeddings, chunks)

query = "What optimizer was used?"

query_embedding = embedder.embed_query(query)

results = vector_store.search(query_embedding)

print("=" * 60)

print(f"Retrieved {len(results)} chunks")

print("=" * 60)

for i, result in enumerate(results):

    print(f"\nResult {i+1}")

    print("Page:", result["page"])

    print(result["text"][:300])