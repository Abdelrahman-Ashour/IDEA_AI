import streamlit as st
from pages import customer_service
from pages import history
from pages import idea

st.set_page_config(page_title="IDEA AI", layout="wide")

pages = {
    "Customer Service": customer_service.app,
    "History": history.app,
    "Idea Finder": idea.app,  # تأكد من أن app موجود في idea_finder.py
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))
pages[selection]()  # استدعاء الدالة المناسبة بناءً على الاختيار
