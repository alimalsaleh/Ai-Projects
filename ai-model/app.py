import os
from pathlib import Path

import pdfplumber
from google import genai


def get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Export GEMINI_API_KEY=your_key before running this script."
        )
    return genai.Client(api_key=api_key)


def simplify_text_from_pdf(pdf_path):
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    full_text = ""
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            full_text += text + "\n"

    if not full_text.strip():
        raise ValueError(f"No readable text found in PDF: {pdf_path}")

    prompt = (
        "Please simplify the following text, explain difficult vocabulary, and summarize it in clear English bullet points:\n\n"
        + full_text
    )

    client = get_client()
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text


if __name__ == "__main__":
    pdf_path = Path(__file__).resolve().parent / "sample.pdf"
    simplified_output = simplify_text_from_pdf(pdf_path)
    print(simplified_output)
