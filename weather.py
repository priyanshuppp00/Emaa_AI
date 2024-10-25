import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def speak_weather(data):
    main = data['weather'][0]['main']
    temp = data['main']['temp']
    print(f"Current weather in {data['name']}: {main} at {temp}°C")
