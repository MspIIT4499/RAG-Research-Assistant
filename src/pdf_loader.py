import fitz  # PyMuPDF
from typing import List, Dict


class PDFLoader:
    """
    Loads PDF files and extracts text page by page.
    """

    def load_pdf(self, pdf_file) -> List[Dict]:
        """
        Reads a PDF and returns page-wise text with metadata.

        Returns:
        [
            {
                "page": 1,
                "text": "...",
                "source": "paper.pdf"
            },
            ...
        ]
        """

        document = fitz.open(stream=pdf_file.read(), filetype="pdf")

        pages = []

        for page_number, page in enumerate(document):

            text = page.get_text()

            pages.append(
                {
                    "page": page_number + 1,
                    "text": text,
                    "source": pdf_file.name
                }
            )

        return pages