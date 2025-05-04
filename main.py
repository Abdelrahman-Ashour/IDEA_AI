import streamlit as st
from pages import idea_finder, customer_service, history

st.set_page_config(page_title="Startup Idea Finder", layout="wide")

pages = {
    "Idea Finder": idea_finder.app,
    "Customer Service": customer_service.app,
    "History": history.app,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))
pages[selection]()