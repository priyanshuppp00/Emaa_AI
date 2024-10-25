import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to female voice (if available)

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for voice commands and returns them as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print("Listening for your command...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio, language='en-IN')
                print(f"You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                speak("Could not request results from Google Speech Recognition service.")
                return ""
            except Exception as e:
                speak(f"An error occurred: {str(e)}")
                return ""

def detect_language(text):
    """Detects the language of the given text."""
    import langdetect
    return langdetect.detect(text)
