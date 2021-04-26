from django.shortcuts import render
import requests

# Create your views here.

API_KEY = '71f3912639934f71b11f94926c92a122'


def index(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if category :
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'

    elif country :
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    return render(request, "news.html", {'articles': articles, 'data': data})
