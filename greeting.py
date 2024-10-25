from voice_recognition import speak

def greet_user(language='en'):
    if language == 'hi':
        greeting_text = "नमस्ते! मैं आपकी कैसे सहायता कर सकती हूँ?"
    else:
        greeting_text = "Hello! How can I assist you today?"

    speak(greeting_text)
