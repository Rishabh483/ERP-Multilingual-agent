import streamlit as st
import speech_recognition as sr
import threading
import azure.cognitiveservices.speech as speechsdk
from modules.config import AZURE_API_KEY, AZURE_REGION

# Initialize the speech config
speech_config = speechsdk.SpeechConfig(subscription=AZURE_API_KEY, region=AZURE_REGION)
speech_config.speech_synthesis_voice_name = "hi-IN-AnanyaNeural"  # Set to Hindi voice
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

def text_to_speech(text):
    try:
        result = speech_synthesizer.speak_text_async(text).get()
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            st.success("Speech synthesis succeeded.")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            st.error(f"Speech synthesis canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                st.error(f"Error details: {cancellation_details.error_details}")
    except Exception as e:
        st.error(f"Azure TTS Error: {str(e)}")

def speech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.session_state.status = "Listening... Please speak now."
            r.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise

            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=10)  # Limit listening time
                st.session_state.status = "Processing speech..."
            except sr.WaitTimeoutError:
                st.session_state.status = "Listening timed out. Please try again."
                return ""

        # Try Hindi first, then fallback to English
        for lang in ['hi-IN', 'en-US']:
            try:
                text = r.recognize_google(audio, language=lang)
                st.session_state.status = ""
                return text
            except sr.UnknownValueError:
                st.session_state.status = f"Could not understand speech in {lang}."
            except sr.RequestError:
                st.session_state.status = "Speech recognition service unavailable. Check your internet connection."
                return ""

        return ""  # If both languages fail, return empty string

    except Exception as e:
        st.session_state.status = f"STT Error: {str(e)}"
        return ""
def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))


def start_listening():
    if not st.session_state.is_listening:
        st.session_state.is_listening = True
        threading.Thread(target=listen_and_update).start()

def listen_and_update():
    text = speech_to_text()
    st.session_state.speech_input = text
    st.session_state.is_listening = False
    st.rerun()
