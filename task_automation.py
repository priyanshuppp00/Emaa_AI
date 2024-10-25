import os
import webbrowser
from email.mime.text import MIMEText
import smtplib

def open_application(app_name):
    if app_name.lower() == "notepad":
        os.system("notepad.exe")
    elif app_name.lower() == "chrome":
        os.system("start chrome")
    else:
        print(f"No instructions for {app_name}")

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "your_email@gmail.com"
    msg["To"] = to

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("your_email@gmail.com", "your_password")
        server.sendmail("your_email@gmail.com", to, msg.as_string())

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def open_website(website):
    url = f"https://{website}"
    webbrowser.open(url)
