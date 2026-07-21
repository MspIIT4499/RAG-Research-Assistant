from pathlib import Path

from dotenv import dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI

from src.prompts import SYSTEM_PROMPT


class ResearchAssistant:
    """
    Handles interaction with the Gemini LLM.
    """

    def __init__(self):

        # Project root directory
        ROOT_DIR = Path(__file__).resolve().parent.parent

        # Load .env
        ENV_PATH = ROOT_DIR / ".env"

        config = dotenv_values(ENV_PATH)

        api_key = config.get("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY not found in .env file"
            )

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash",
            google_api_key=api_key,
            temperature=0.2,
        )

    def answer(self, question, retrieved_chunks):

        context = "\n\n".join(
            f"Page {chunk['page']}\n{chunk['text']}"
            for chunk in retrieved_chunks
        )

        prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.llm.invoke(prompt)

        
        if isinstance(response.content, list):
            return "\n".join(
                part["text"]
                for part in response.content
                if isinstance(part, dict) and part.get("type") == "text"
             )

        return response.content