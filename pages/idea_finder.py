import streamlit as st
from datetime import datetime
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fpdf import FPDF
from io import BytesIO
import os

def send_email(user_email, subject, message):
    try:
        sender_email = os.getenv("SENDER_EMAIL")
        receiver_email = user_email
        password = os.getenv("EMAIL_PASSWORD")

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        st.success("تم إرسال البريد الإلكتروني بنجاح.")
    except Exception as e:
        st.error(f"فشل إرسال البريد الإلكتروني: {str(e)}")

def save_to_pdf(user_data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="تقرير فكرة المشروع", ln=True, align="C")
    pdf.ln(10)

    for key, value in user_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    # Save PDF to a BytesIO object instead of a file path
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return pdf_output

def show():
    st.title("ابحث عن فكرة مشروع")

    user_name = st.text_input("الاسم الكامل:")
    user_email = st.text_input("البريد الإلكتروني:")
    budget = st.number_input("الميزانية المتاحة (جنيه)", min_value=0, step=1000)
    skills = st.text_area("المهارات المتوفرة:")
    competition = st.number_input("معدل التنافس في السوق (من 1 إلى 10)", min_value=1, max_value=10)

    if st.button("اعرض فكرة المشروع"):
        if user_name and user_email and skills and budget and competition:
            idea = f"مشروع برمجي استنادًا إلى مهاراتك: بناء تطبيق باستخدام الذكاء الاصطناعي لخدمة العملاء."
            user_data = {
                "الاسم": user_name,
                "البريد الإلكتروني": user_email,
                "الميزانية": budget,
                "المهارات": skills,
                "التنافس في السوق": competition,
                "الفكرة": idea
            }

            # إرسال تقرير فكرة المشروع عبر البريد الإلكتروني
            send_email(user_email, "فكرة مشروعك", f"نحن نقترح عليك فكرة مشروع برمجي بناءً على مهاراتك: {idea}")

            # حفظ التقرير في PDF
            pdf_output = save_to_pdf(user_data)
            st.download_button("تحميل التقرير بصيغة PDF", pdf_output, file_name="project_idea_report.pdf")

            st.success(f"تم اقتراح الفكرة بنجاح! اطلع على التقرير المرفق.")
        else:
            st.error("يرجى تعبئة جميع الحقول.")
