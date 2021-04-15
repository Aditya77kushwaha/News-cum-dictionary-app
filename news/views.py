from django.shortcuts import render
import requests

# Create your views here.

API_KEY = '71f3912639934f71b11f94926c92a122'


def index(request):
    url = f'https://newsapi.org/v2/everything?q=Apple&from=2021-04-15&sortBy=popularity&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return render(request, "news.html", {'articles': articles, 'data': data})
