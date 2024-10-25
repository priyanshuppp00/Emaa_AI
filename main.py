import tkinter as tk
from task_handler import handle_task
from voice_recognition import listen, speak, detect_language
from security import verify_name, put_emaa_to_sleep, wake_emaa_up
from greeting import greet_user

def show_popup():
    """Shows a popup window when Emaa is active."""
    root = tk.Tk()
    root.title("Emaa is Active")
    label = tk.Label(root, text="How can I help you?", font=("Helvetica", 16))
    label.pack(pady=5)
    command_text = tk.Text(root, height=15, width=40)
    command_text.pack(pady=10)
    root.geometry("400x300")
    return root, command_text

def bring_popup_to_front(popup):
    """Brings the popup window to the front."""
    popup.lift()
    popup.attributes('-topmost', True)
    popup.after_idle(popup.attributes, '-topmost', False)

def display(text, command_text):
    """Displays text in the popup window and logs to the terminal."""
    print(text)  # Logs to the terminal
    command_text.insert(tk.END, f"{text}\n")
    command_text.see(tk.END)  # Scroll to the end
    command_text.update_idletasks()  # Ensure the display updates in real-time

def sleep_mode(command_text):
    """Puts Emaa into sleep mode and waits for wake word."""
    display("Emaa: Going to sleep mode. Say 'Emaa' to wake me up.", command_text)
    while True:
        command = listen()
        if "emaa" in command.lower():
            display("Emaa: I'm here.", command_text)
            speak("I'm here.")
            return

def start_emaa():
    """Starts Emaa and listens for commands."""
    popup, command_text = show_popup()
    bring_popup_to_front(popup)
    popup.update_idletasks()
    popup.update()  
    if not verify_name():
        display("Emaa: Verification failed.", command_text)
        popup.destroy()
        return
    while True:
        display("Emaa: Listening for your command.", command_text)
        speak("Listening for your command.")
        
        command = listen()
        if command:
            display(f"Emaa: Listening... You said: {command}", command_text)
            language = detect_language(command)
            display(f"You: {command}", command_text)
            if "stop" in command or "exit" in command or "quit" in command:
                display("Emaa: Goodbye! Have a great day, Priyanshu!", command_text)
                speak("Goodbye! Have a great day, Priyanshu!")
                return
            if "go to sleep" in command:
                display("Emaa: Going to sleep mode.", command_text)
                speak("Going to sleep mode.")
                sleep_mode(command_text)
                continue
            if handle_task(command, language, command_text):
                break
        popup.update_idletasks()
        popup.update()

if __name__ == "__main__":
    try:
        start_emaa()
    except KeyboardInterrupt:
        exit_message = "Exiting Emaa. Have a great day, Priyanshu!"
        speak(exit_message)
        if 'command_text' in locals():
            display(exit_message, command_text)
