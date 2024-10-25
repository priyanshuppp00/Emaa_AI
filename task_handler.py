import os
import datetime
import tkinter as tk
import webbrowser
from voice_recognition import speak
from security import lock_pc, shutdown_pc
from weather import get_weather
from news import get_news

def log_interaction(details, command_text):
    """Logs interactions to a file and displays in the popup window."""
    with open("interaction_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()}: {details}\n")
    if command_text and command_text.winfo_exists():
        command_text.insert(tk.END, f"{details}\n")

def open_application(app_name):
    """Opens the specified application."""
    try:
        if app_name.lower() == "notepad":
            os.system("notepad.exe")
            response = "Opening Notepad."
        elif app_name.lower() == "chrome":
            os.system("start chrome")
            response = "Opening Chrome."
        elif app_name.lower() == "calculator":
            os.system("calc.exe")
            response = "Opening Calculator."
        elif app_name.lower() == "explorer":
            os.system("explorer.exe")
            response = "Opening File Explorer."
        else:
            response = f"No instructions for {app_name}."
        speak(response)
    except Exception as e:
        response = f"An error occurred while trying to open {app_name}: {str(e)}"
    return response

def handle_task(command, language, command_text):
    """Handles a given task command."""
    try:
        if "search" in command:
            query = command.replace("search", "").strip()
            search_google(query)
            response = f"Searching for {query} on Google."
        elif "open" in command:
            website = command.replace("open", "").strip()
            open_website(website)
            response = f"Opening {website}."
        elif "lock my computer" in command or "lock laptop" in command:
            lock_pc()
            response = "Locking the computer."
        elif "shut down my laptop" in command or "turn off laptop" in command or "laptop band kro" in command:
            shutdown_pc()
            response = "Shutting down the laptop."
        elif "open application" in command:
            app_name = command.replace("open application", "").strip()
            response = open_application(app_name)
        elif "what's the weather" in command:
            weather_data = get_weather("your_openweathermap_api_key", "your_city_name")
            response = f"The current weather is: {weather_data}"
        elif "news" in command:
            articles = get_news("your_newsapi_key")
            response = "Here are the latest news headlines."
        else:
            response = "I didn't catch that. How can I assist you?"
        speak(response, language)
        log_interaction(f"Emaa: {response}", command_text)
    except Exception as e:
        error_response = "I couldn't understand that. Could you please say it again?"
        speak(error_response)
        log_interaction(f"Emaa: {error_response}", command_text)
        log_interaction(f"Emaa: An error occurred: {str(e)}", command_text)

    return False

def search_google(query):
    """Searches Google for the given query."""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the results for {query} on Google.")

def open_website(website):
    """Opens the specified website."""
    url = f"https://{website}"
    webbrowser.open(url)
    speak(f"Opening {website}.")
