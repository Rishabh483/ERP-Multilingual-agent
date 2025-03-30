# Priya AI Sales Agent

Priya is a multilingual conversational AI sales agent built with Streamlit and powered by Google's Gemini model. The application demonstrates how AI can be used in various business contexts including sales, recruitment, and payment collection.
<img width="919" alt="image" src="https://github.com/user-attachments/assets/1fa5262d-8b29-4dbe-a330-0f2195807a54" />

<img width="919" alt="image" src="https://github.com/user-attachments/assets/f67a2454-2590-4d44-917f-acece2aa8835" />


## Features

### 1. Multi-Module Conversation System
- **ERP Sales**: Priya can act as a sales representative for SmartBiz ERP, convincing potential customers to schedule demos.
- **Job Interview**: Priya can conduct screening interviews for AI/ML Engineer positions.
- **Payment Collection**: Priya can follow up with customers regarding pending payments.

### 2. Multilingual Support
- Supports conversations in Hindi-English mix (Hinglish)
- Voice recognition works with both Hindi and English inputs
- Text-to-speech capability with an Indian accent voice

### 3. Voice Interaction
- Speech-to-text functionality using Google's Speech Recognition
- Text-to-speech using Azure Cognitive Services
- Microphone input for hands-free interaction

### 4. User Interface
- Clean, intuitive Streamlit interface
- Real-time conversation display
- Module selection buttons
- Status indicators for voice recognition

### 5. Conversation Memory
- Maintains conversation history within each session
- Context-aware responses based on conversation history
- Session state management

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 1.5 Flash (via LangChain)
- **Speech Services**:
  - Speech Recognition (Google)
  - Text-to-Speech (Azure Cognitive Services)
- **Languages**: Python, HTML/CSS (via Streamlit)

## Project Structure

```
project/
│
├── app.py                  # Main application entry point
├── modules/
│   ├── __init__.py
│   ├── session_state.py    # Session state management
│   ├── ui.py               # UI components and layout
│   ├── audio.py            # Speech-to-text and text-to-speech functions
│   ├── conversation.py     # Conversation handling logic
│   ├── gemini.py           # Integration with Google Gemini API
│   ├── product_data.py     # Sample data for different modules
│   └── config.py           # API keys and configuration
```

## Installation

1. Clone the repository:
```
git clone https://github.com/AmarBackInField/IMax_Assignment.git
conda create -p rec python=3.10 -y
conda activate rec
pip install -r requirements.txt
```

2. Install required packages:
```
pip install streamlit
pip install SpeechRecognition
pip install PyAudio
pip install langchain_google_genai
pip install google-api-python-client
pip install google-auth
pip install azure-cognitiveservices-speech
```

3. Set up your API keys:
   - Get a Google API key for Gemini
   - Get Azure Speech Service API key
   - Update the `config.py` file with your keys

## Usage

1. Start the application:
```
streamlit run app.py
```

2. Enter your Google API key in the sidebar.

3. Select a conversation module (ERP Sales, Job Interview, or Payment Collection).

4. Start interacting with Priya through text or by using the microphone button.

## Conversation Flows

### ERP Sales
Priya will try to convince potential customers to schedule a demo for SmartBiz ERP by highlighting features and benefits tailored to their needs.

### Job Interview
Priya will conduct screening interviews for AI/ML Engineer positions, asking about experience, skills, and technical knowledge.

### Payment Collection
Priya will follow up with customers who have pending payments, maintaining a professional but persistent approach.

## Customization

You can customize the agent's behavior by modifying:
- `product_data.py`: Change product information, job details, or customer data
- `gemini.py`: Adjust the system prompts for different conversation modules
- `audio.py`: Change voice settings or speech recognition parameters

## Note on API Keys

- The application requires a Google API key for accessing the Gemini model.
- Azure Speech Services credentials are needed for text-to-speech functionality.
- For security reasons, avoid hardcoding keys in production environments.

## Incomplete Parts:
Connect google calender api , as there is some issue with the key, So i leaved it, but all other parts have completed.


