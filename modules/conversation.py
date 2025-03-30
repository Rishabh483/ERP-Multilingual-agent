import streamlit as st
from modules.gemini import get_erp_response, get_job_response, get_payment_response
from modules.product_data import product_data
import threading
from modules.audio import text_to_speech  # Import text_to_speech

def get_agent_response(user_input, module):
    if module == "ERP Sales":
        return get_erp_response(user_input)
    elif module == "Job Interview":
        return get_job_response(user_input)
    elif module == "Payment Collection":
        return get_payment_response(user_input)
    else:
        return "Module not selected. Please select a module first."

def handle_submit():
    user_message = st.session_state.user_input
    if user_message and st.session_state.selected_module:
        process_user_message(user_message)

def process_user_message(user_message):
    if user_message and st.session_state.selected_module:
        st.session_state.conversation_history.append({"role": "user", "content": user_message})
        st.session_state.chat_memory.append({"role": "user", "content": user_message})
        agent_response = get_agent_response(user_message, st.session_state.selected_module)
        st.session_state.conversation_history.append({"role": "assistant", "content": agent_response})
        st.session_state.chat_memory.append({"role": "assistant", "content": agent_response})
        threading.Thread(target=text_to_speech, args=(agent_response,)).start()

def set_module(module):
    st.session_state.selected_module = module
    st.session_state.conversation_history = []
    st.session_state.chat_memory = []
    if module == "ERP Sales":
        initial_message = product_data["erp"]["sample_dialogues"][0]["agent"]
    elif module == "Job Interview":
        initial_message = product_data["job"]["sample_dialogues"][0]["agent"]
    elif module == "Payment Collection":
        initial_message = "Namaste! Main payment follow-up ke liye aapki madad kar sakta hoon. Kis customer ke baare mein baat karni hai?"
    st.session_state.conversation_history.append({"role": "assistant", "content": initial_message})
    st.session_state.chat_memory.append({"role": "assistant", "content": initial_message})
    threading.Thread(target=text_to_speech, args=(initial_message,)).start()
