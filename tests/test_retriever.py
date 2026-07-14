from src.retriever import Retriever

retriever = Retriever()

query = "What optimizer is used?"

results = retriever.retrieve(query)

print("=" * 60)

print(f"Retrieved {len(results)} chunks")

print("=" * 60)

for i, chunk in enumerate(results):

    print(f"\nChunk {i+1}")

    print("Page:", chunk["page"])

    print(chunk["text"][:400])