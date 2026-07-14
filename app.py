import streamlit as st

st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Research Paper Assistant")

st.write(
    "Upload one or more research papers and ask questions about them."
)

uploaded_files = st.file_uploader(
    "Upload PDF(s)",
    type=["pdf"],
    accept_multiple_files=True
)

question = st.text_input(
    "Ask a question about your papers"
)

if st.button("Ask"):
    if uploaded_files is None or len(uploaded_files) == 0:
        st.warning("Please upload at least one PDF.")
    elif question == "":
        st.warning("Please enter a question.")
    else:
        st.success("Everything is working! We'll connect the AI next.")