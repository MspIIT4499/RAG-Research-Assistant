import streamlit as st

from src.research_tools import ResearchTools


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)


# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------

if "tools" not in st.session_state:
    st.session_state.tools = ResearchTools()

if "processed" not in st.session_state:
    st.session_state.processed = False

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("📚 AI Research Paper Assistant")
st.caption("Chat with your research papers using Retrieval-Augmented Generation (RAG)")


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.header("📂 Document Management")

    uploaded_files = st.file_uploader(
        "Upload PDF(s)",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button(
        "📄 Process Papers",
        use_container_width=True
    ):

        if not uploaded_files:

            st.warning("Please upload at least one PDF.")

        else:

            with st.spinner("Processing research papers..."):

                st.session_state.tools.process(uploaded_files)

                st.session_state.processed = True

                st.session_state.messages = []

            st.success("Knowledge base created successfully!")

    st.divider()

    st.subheader("Status")

    if st.session_state.processed:

        st.success("✅ Ready")

        st.write(f"📄 **Documents:** {len(uploaded_files)}")

    else:

        st.info("Waiting for PDFs")

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


# ---------------------------------------------------------
# Display Chat History
# ---------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ---------------------------------------------------------
# Chat Input
# ---------------------------------------------------------

question = st.chat_input(
    "Ask a question about your research papers...",
    disabled=not st.session_state.processed
)


# ---------------------------------------------------------
# Generate Response
# ---------------------------------------------------------

if question:

    # Display User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # Generate AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = st.session_state.tools.ask(question)

        st.markdown(answer)

    # Save AI Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )