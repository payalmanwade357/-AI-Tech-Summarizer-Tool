```python
import streamlit as st
from utils import summarize_text, read_pdf, read_docx

# Page Configuration
st.set_page_config(
    page_title="Tech Summarizer",
    page_icon="📝",
    layout="wide"
)

# Title
st.title("📝 AI Tech Summarizer Tool")
st.write("Summarize Technical Articles, Blogs, PDFs and DOCX Files")

# Select Input Type
option = st.radio(
    "Choose Input Type",
    ["Text", "PDF", "DOCX"]
)

text = ""

# Text Input
if option == "Text":
    text = st.text_area(
        "Paste your article",
        height=300
    )

# PDF Input
elif option == "PDF":
    pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if pdf:
        text = read_pdf(pdf)

# DOCX Input
elif option == "DOCX":
    doc = st.file_uploader(
        "Upload DOCX",
        type=["docx"]
    )

    if doc:
        text = read_docx(doc)

# Generate Summary
if st.button("Generate Summary"):

    if not text.strip():
        st.warning("Please provide some text.")

    else:
        with st.spinner("Generating Summary..."):
            try:
                summary = summarize_text(text)

                st.subheader("📌 Summary")
                st.success(summary)

                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error while generating summary: {e}")
```


       
