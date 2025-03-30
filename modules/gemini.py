import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from modules.product_data import product_data

def get_erp_response(user_input):
    system_prompt = f"""Tum Priya ho, SmartBiz ERP ke sales representative.
    Tumhe customer ko convince karna hai ki wo demo ke liye agree karein.
    Jab customer ready ho, unse email lo aur meeting schedule karo.
    Yeh product details hain: {product_data['erp']['product_info']}

    Responses should be in Hindi-English mix (Hinglish), professional but friendly.
    Keep responses under 3-4 sentences and try to move towards getting a demo scheduled.
    """
    return get_gemini_response(user_input, system_prompt, st.session_state.chat_memory)

def get_job_response(user_input):
    system_prompt = f"""Tum Priya ho, iMax Global Ventures ke liye AI/ML Engineer candidates ka interview le rahe ho.
    Hindi aur English dono mein baat kar sakte ho. Professional but friendly rahein.

    Job details: {product_data['job']['job_details']}
    Screening questions to cover: {product_data['job']['screening_questions']}

    Keep responses under 3-4 sentences and ask relevant technical questions about AI/ML experience.
    """
    return get_gemini_response(user_input, system_prompt, st.session_state.chat_memory)

def get_payment_response(user_input):
    system_prompt = f"""Tum Priya ho, iMax Global Ventures ke payment collection team se.
    Tumhe customers se pending payments follow-up karna hai.
    Yeh customer details hain: {product_data['payment']['customer_details']}

    Hindi-English mix (Hinglish) mein baat karo, professional but persistent rahein.
    Keep responses under 3-4 sentences and focus on getting payment commitment.
    """
    return get_gemini_response(user_input, system_prompt, st.session_state.chat_memory)


def get_gemini_response(user_input, system_prompt, chat_memory):
    if not st.session_state.api_key:
        return "API key missing. Please enter your Google API key in the sidebar."
    messages = [SystemMessage(content=system_prompt)]
    for message in chat_memory:
        if message["role"] == "user":
            messages.append(HumanMessage(content=message["content"]))
        else:
            messages.append(AIMessage(content=message["content"]))
    messages.append(HumanMessage(content=user_input))
    try:
        model = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash-8b",
            temperature=0.3,
            google_api_key=st.session_state.api_key,
            max_tokens=30
        )
        response = model.invoke(messages)
        return response.content if response else "Maaf kijiye, main samajh nahi paaya. Kripya phir se poochhein."
    except Exception as e:
        return f"Error: {str(e)}"
