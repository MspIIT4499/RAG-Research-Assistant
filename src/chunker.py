from langchain_text_splitters import RecursiveCharacterTextSplitter

class Chunker:
    """
    Splits page-wise document text into overlapping chunks
    while preserving page and source metadata.
    """

    def __init__(self, chunk_size=800, chunk_overlap=150):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_documents(self, pages):

        chunks = []

        for page in pages:

            page_chunks = self.text_splitter.split_text(page["text"])

            for chunk in page_chunks:

                chunks.append({
                    "text": chunk,
                    "page": page["page"],
                    "source": page["source"]
                })

        return chunks