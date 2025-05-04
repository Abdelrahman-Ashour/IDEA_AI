from fpdf import FPDF
import uuid

def save_to_pdf(question, answer):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    text = f"Question:\n{question}\n\nAnswer:\n{answer}"
    pdf.multi_cell(0, 10, text)

    filename = f"/mnt/data/{uuid.uuid4()}.pdf"
    pdf.output(filename)
    return filename
