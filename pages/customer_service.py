import streamlit as st
from utils.db import store_qa
from utils.pdf_generator import save_to_pdf
from utils.email_sender import send_email
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

def app():
    st.title("Customer Service")

    user_question = st.text_area("💬 Write your question here:")
    user_email = st.text_input("📧 Your email (to receive PDF):")

    if st.button("Send"):
        if not user_question:
            st.error("Please write a question.")
            return

        with st.spinner("Getting your answer..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_question}
                ]
            )
            answer = response["choices"][0]["message"]["content"]

        st.success("✅ Response received:")
        st.write(answer)

        store_qa(user_question, answer)
        pdf_path = save_to_pdf(user_question, answer)
        if user_email:
            send_email(user_email, pdf_path)
