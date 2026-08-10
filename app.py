import streamlit as st
from utils import summarize_text, read_pdf, read_docx

st.set_page_config(
    page_title="Tech Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 AI Tech Summarizer Tool")

st.write("Summarize Technical Articles, Blogs, PDFs and DOCX Files")

option = st.radio(
    "Choose Input Type",
    ["Text", "PDF", "DOCX"]
)

text = ""

if option == "Text":
    text = st.text_area(
        "Paste your article",
        height=300
    )

elif option == "PDF":
    pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if pdf:
        text = read_pdf(pdf)

elif option == "DOCX":
    doc = st.file_uploader(
        "Upload DOCX",
        type=["docx"]
    )

    if doc:
        text = read_docx(doc)

if st.button("Generate Summary"):

    if text.strip() == "":
        st.warning("Please provide some text.")
    else:

        with st.spinner("Generating Summary..."):

            summary = summarize_text(text)

        st.subheader("Summary")

        st.success(summary)

        st.download_button(
            "Download Summary",
            summary,
            file_name="summary.txt"
        )