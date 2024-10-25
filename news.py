import requests

def get_news(api_key, category='general'):
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['articles']

def speak_news(articles):
    for article in articles[:5]:
        print(article['title'])
