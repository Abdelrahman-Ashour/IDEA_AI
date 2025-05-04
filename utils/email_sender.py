import smtplib
from email.message import EmailMessage
import os

def send_email(to_email, file_path):
    msg = EmailMessage()
    msg["Subject"] = "Your Startup Idea Q&A Report"
    msg["From"] = os.getenv("EMAIL_FROM", "noreply@example.com")
    msg["To"] = to_email
    msg.set_content("Attached is your Q&A report.")

    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="report.pdf")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_FROM"), os.getenv("EMAIL_PASSWORD"))
        smtp.send_message(msg)