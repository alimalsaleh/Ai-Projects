import pdfplumber
from google import genai

# تمهيد العميل
client = genai.Client()

def simplify_text_from_pdf(pdf_path):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"

    # إضافة توجيه للنموذج لتنسيق المخرجات بشكل مرتب
    prompt = (
        "Please simplify the following text, explain difficult vocabulary, and summarize in clear English points"
        + full_text
    )

    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
    )

    return response.text

pdf_path = "sample.pdf"
simplified_output = simplify_text_from_pdf(pdf_path)

print(simplified_output)