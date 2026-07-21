from src.pdf_loader import PDFLoader
from src.chunker import Chunker
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.retriever import Retriever
from src.llm import ResearchAssistant


class ResearchTools:
    """
    High-level interface for the Research Paper Assistant.

    The frontend only interacts with this class.
    """

    def __init__(self):
        self.loader = PDFLoader()
        self.chunker = Chunker()
        self.embedder = EmbeddingModel()
        self.vector_store = VectorStore()

        self.retriever = None
        self.assistant = ResearchAssistant()

    def process(self, uploaded_files):
        """
        Process uploaded PDFs and build the vector store.
        """

        all_pages = []

        for pdf in uploaded_files:
            pages = self.loader.load_pdf(pdf)
            all_pages.extend(pages)

        chunks = self.chunker.split_documents(all_pages)

        embeddings = self.embedder.embed_documents(chunks)

        self.vector_store.create_index(
            embeddings,
            chunks
)

        self.retriever = Retriever(
            self.vector_store,
            self.embedder
)

    def ask(self, question):
        """
        Retrieve relevant chunks and generate an answer.
        """

        chunks = self.retriever.retrieve(question)

        return self.assistant.answer(
            question,
            chunks
        )