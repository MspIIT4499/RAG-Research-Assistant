from src.retriever import Retriever
from src.llm import ResearchAssistant


retriever = Retriever()

assistant = ResearchAssistant()


question = "What optimizer is used?"


chunks = retriever.retrieve(question)


answer = assistant.answer(

    question,

    chunks

)


print("=" * 60)

print(answer)