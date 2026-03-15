import streamlit as st
from src import get_faq_quetion


st.set_page_config(page_title="ML FAQ BOT", layout='centered')
st.title("Machine Learning FAQ Bot")

user_input = st.text_input("Ask anything about ML:")

if user_input:
    answer = get_faq_quetion(user_input)
    st.write(answer)