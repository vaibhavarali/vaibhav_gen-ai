import streamlit as st
from typing import Generator
from groq import Groq

st.set_page_config(page_icon="💬", layout="wide",
                   page_title="PragyanAI Groq Streamlit APP")
# Display the logo at the top of the page

st.divider()  # 👈 Draws a horizontal rule

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


#icon("🏎")

st.subheader("Groq Chat Streamlit App", divider="rainbow", anchor=False)

#GROQ_API_KEY = "your_groq_api_key_here"
