import streamlit as st

def layout():
    st.title("Hi, I'm Priya")

def sidebar():
    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input("Enter Google API Key:", type="password")
        if api_key:
            st.session_state.api_key = api_key
            st.success("API Key set!")

        st.title("About")
        st.info(
            """
            **Priya AI Agent**

            This application demonstrates a conversational AI agent powered by Gemini that can:
            - Sell SmartBiz ERP solutions
            - Conduct job interviews for AI/ML positions
            - Follow up on payment collections

            The agent uses both Hindi and English (Hinglish) based on context.
            """
        )

        st.title("Required Packages")
        st.code("""
        pip install streamlit
        pip install SpeechRecognition
        pip install pyttsx3
        pip install PyAudio
        pip install langchain_google_genai
        pip install google-api-python-client
        pip install google-auth
        """)
