import streamlit as st
from modules.session_state import initialize_session_state
from modules.ui import layout, sidebar
from modules.audio import start_listening, speech_to_text, voice_input
from modules.conversation import handle_submit, process_user_message, set_module
from modules.product_data import product_data

# Initialize session state variables
initialize_session_state()

# Set page config
st.set_page_config(page_title="Priya - AI Sales Agent", layout="wide")

# Layout the UI
layout()

# Sidebar for API key and about info
sidebar()

# Module selection
st.subheader("Choose a conversation module:")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("ERP Sales", use_container_width=True, key="erp"):
        set_module("ERP Sales")
with col2:
    if st.button("Job Interview", use_container_width=True, key="job"):
        set_module("Job Interview")
with col3:
    if st.button("Payment Collection", use_container_width=True, key="payment"):
        set_module("Payment Collection")

# Display selected module
if st.session_state.selected_module:
    st.markdown(f"**Current Mode:** {st.session_state.selected_module}")

# Display conversation history
st.subheader("Conversation History")
conversation_container = st.container()
with conversation_container:
    for message in st.session_state.conversation_history:
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}")
        elif message["role"] == "assistant":
            st.markdown(f"**Priya:** {message['content']}")

# Display status if listening
if st.session_state.status:
    st.info(st.session_state.status)

# User input section
st.subheader("Your Message")
col1, col2 = st.columns([5, 1])

# Check if we have speech input from the microphone
if st.session_state.speech_input:
    input_value = st.session_state.speech_input
    st.session_state.speech_input = ""
else:
    input_value = ""

with col1:
    user_input = st.text_input(
        "Type your message:",
        key="user_input",
        value=st.session_state.get("input_value", ""),
        on_change=handle_submit
    )

with col2:
    mic_button = st.button("🎤", help="Speak", disabled=st.session_state.is_listening or not st.session_state.selected_module)
    if mic_button:
        response = voice_input()
        if response:
            st.session_state.input_value = response  # Update the input field with voice response
            st.rerun()  # Trigger re-render to update the text input field

# Submit button - only process if there's text in the input field
if st.button("Send", disabled=not st.session_state.selected_module):
    if st.session_state.user_input:
        process_user_message(st.session_state.user_input)
