from src.pdf_loader import PDFLoader
from src.chunker import Chunker

loader = PDFLoader()
chunker = Chunker()

with open("data/attention.pdf", "rb") as pdf:

    pages = loader.load_pdf(pdf)

chunks = chunker.split_documents(pages)

print("=" * 50)
print(f"Pages Loaded : {len(pages)}")
print(f"Chunks Created : {len(chunks)}")
print("=" * 50)

print("\nFirst Chunk:\n")
print(chunks[0]["text"][:500])

print("\nMetadata:")
print(chunks[0]["page"])
print(chunks[0]["source"])