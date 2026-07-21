import streamlit as st

from src.research_tools import ResearchTools


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)


# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "tools" not in st.session_state:
    st.session_state.tools = ResearchTools()

if "processed" not in st.session_state:
    st.session_state.processed = False


# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("📚 AI Research Paper Assistant")

st.write(
    "Upload one or more research papers and ask questions about them."
)


# ---------------------------------------------------
# Upload PDFs
# ---------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload PDF(s)",
    type=["pdf"],
    accept_multiple_files=True
)


# ---------------------------------------------------
# Process Papers
# ---------------------------------------------------

if st.button("📄 Process Papers"):

    if not uploaded_files:

        st.warning("Please upload at least one PDF.")

    else:

        with st.spinner("Processing research papers..."):

            st.session_state.tools.process(uploaded_files)

            st.session_state.processed = True

        st.success("Research papers processed successfully!")


# ---------------------------------------------------
# Ask Question
# ---------------------------------------------------

question = st.text_input(
    "Ask a question about your papers",
    disabled=not st.session_state.processed
)


# ---------------------------------------------------
# Generate Answer
# ---------------------------------------------------

if st.button("💬 Ask"):

    if not st.session_state.processed:

        st.warning("Please process your papers first.")

    elif question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer..."):

            answer = st.session_state.tools.ask(question)

        st.markdown("---")

        st.subheader("Answer")

        st.write(answer)