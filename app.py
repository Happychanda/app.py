import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")


st.set_page_config(page_title="Citizen AI", layout="centered")
st.markdown('<h1 style="color:#00ffff;text-align:center;">🇮🇳 Citizen AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">Ask any question related to your rights, government schemes, and more</p>', unsafe_allow_html=True)

query = st.text_area("Enter your question", height=150)
if st.button("Ask Gemini"):
    if query.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(query)
                st.success("Response from Gemini:")
                st.markdown(f"<div style='background-color:#111;padding:15px;border-radius:10px;color:#00ffff;'>{response.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {str(e)}")