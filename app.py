import streamlit as st
from src import get_faq_quetion

st.markdown("""
    <style>
    /* Title Section Background */
    .header-container {
        background-color: #1E3A8A;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 25px;
    }
    .main-title {
        font-size: 32px;
        color: #FFFFFF !important;
        font-weight: bold;
        margin: 0;
    }
    .sub-title {
        font-size: 16px;
        color: #D1D5DB !important;
        margin: 5px 0 0 0;
    }
    
    /* Style for the Answer Text */
    .answer-text {
        color: #111827; /* Dark color for better readability */
        background-color: #F3F4F6;
        padding: 15px;
        border-left: 5px solid #1E3A8A;
        border-radius: 5px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("Settings & Info")
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.rerun()


st.set_page_config(page_title="ML FAQ BOT", layout='centered')
st.markdown('<p class="main-title">🤖 Machine Learning FAQ Bot</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your instant guide to ML concepts</p>', unsafe_allow_html=True)
st.divider()

user_input = st.chat_input("Ask anything about ML (e.g., What is Overfitting?)")

if user_input:
    # Display User Message
    with st.chat_message("user"):
        st.markdown(f"**You:** {user_input}")
    
    # Display Assistant Response with Loading Spinner
    with st.chat_message("assistant"):
        with st.spinner("Processing your request..."):
            try:
                # Fetching answer from your custom source
                answer = get_faq_quetion(user_input)
                
                if answer:
                    st.markdown(answer)
                else:
                    st.warning("I couldn't find a specific answer for that. Please try another question.")
            
            except Exception as e:
                st.error("Error: The source module could not be reached. Please check your 'src' folder.")

# 6. Default state when no input is provided
else:
    st.info("Start the conversation by typing your question in the box below.")