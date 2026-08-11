```python
import PyPDF2
from docx import Document
from model import summarizer


def summarize_text(text):
    """Generate summary using Hugging Face model."""

    if len(text.strip()) == 0:
        return "Please enter some text."

    # Model works best with limited input length
    text = text[:3000]

    summary = summarizer(
        text,
        max_length=150,
        min_length=40,
        do_sample=False
    )

    return summary[0]["summary_text"]


def read_pdf(file):
    """Extract text from a PDF file."""

    pdf_reader = PyPDF2.PdfReader(file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def read_docx(file):
    """Extract text from a DOCX file."""

    doc = Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text
```

    
   
