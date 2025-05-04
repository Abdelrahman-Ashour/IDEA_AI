from fpdf import FPDF
import uuid
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Cairo", size=12)
        self.cell(0, 10, 'IDEA AI Report', ln=True, align='C')

def save_to_pdf(question, answer):
    pdf = PDF()
    pdf.add_page()

    font_path = os.path.join("utils", "Cairo-Regular.ttf")
    pdf.add_font("Cairo", "", font_path, uni=True)
    pdf.set_font("Cairo", size=12)

    pdf.multi_cell(0, 10, f"Question:\n{question}\n\nAnswer:\n{answer}")
    filename = f"/mnt/data/{uuid.uuid4()}.pdf"
    pdf.output(filename)
    return filename
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
