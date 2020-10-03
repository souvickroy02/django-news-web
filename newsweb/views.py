from django.shortcuts import render

# Create your views here.


def home(request):
    import requests
    import json
    news_api_request = requests.get(
        "http://newsapi.org/v2/top-headlines?country=in&apiKey=bc95026edd334867a18c449a7cf30aaa")
    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api': api})
