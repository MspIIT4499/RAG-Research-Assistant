from src.pdf_loader import PDFLoader

loader = PDFLoader()

with open("data/attention.pdf", "rb") as pdf:
    pages = loader.load_pdf(pdf)

print(f"Total Pages: {len(pages)}")

print("\nFirst Page Metadata:")
print(pages[0]["page"])
print(pages[0]["source"])

print("\nFirst 500 characters:\n")
print(pages[0]["text"][:500])