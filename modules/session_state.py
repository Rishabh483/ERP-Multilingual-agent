import streamlit as st

def initialize_session_state():
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    if 'chat_memory' not in st.session_state:
        st.session_state.chat_memory = []
    if 'selected_module' not in st.session_state:
        st.session_state.selected_module = None
    if 'is_listening' not in st.session_state:
        st.session_state.is_listening = False
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ""
    if 'speech_input' not in st.session_state:
        st.session_state.speech_input = ""
    if 'status' not in st.session_state:
        st.session_state.status = ""
