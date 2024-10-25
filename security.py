import os
import sys
import time
from voice_recognition import listen, speak

def lock_pc():
    """Locks the computer."""
    speak("Locking the computer for security.")
    if sys.platform.startswith('win'):
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif sys.platform.startswith('linux'):
        os.system("gnome-screensaver-command -l")
    elif sys.platform.startswith('darwin'):
        os.system("pmset displaysleepnow")

def shutdown_pc():
    """Shuts down the computer."""
    speak("Shutting down the laptop.")
    if sys.platform.startswith('win'):
        os.system("shutdown /s /t 1")
    elif sys.platform.startswith('linux'):
        os.system("shutdown now")
    elif sys.platform.startswith('darwin'):
        os.system("sudo shutdown -h now")

def verify_name():
    """Verifies the user's name with up to 3 retries."""
    speak("Welcome! My name is Emaa. Please verify your name.")
    retries = 3
    while retries > 0:
        name = listen()
        if "priyanshu" in name:
            speak("Welcome, Priyanshu! How can I help you today?")
            return True
        else:
            retries -= 1
            speak(f"Name not recognized. You have {retries} attempt{'s' if retries > 1 else ''} remaining.")
    speak("Verification failed. Locking the computer for security.")
    lock_pc()
    return False

def put_emaa_to_sleep():
    """Puts Emaa into sleep mode."""
    speak("Going to sleep mode.")

def wake_emaa_up():
    """Wakes Emaa up from sleep mode."""
    speak("I'm here.")
