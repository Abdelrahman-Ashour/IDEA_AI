import streamlit as st
from utils.db import get_history

def app():
    st.title("History of Q&A")
    data = get_history()

    if not data:
        st.write("No questions asked yet.")
        return

    for question, answer in data:
        st.markdown(f"**Q:** {question}")
        st.markdown(f"**A:** {answer}")
        st.markdown("---")
