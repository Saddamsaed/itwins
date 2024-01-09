from django.shortcuts import render
import requests



def say_hello(request):
    requests.get('https://httpbin.org/')
    return render(request, 'hello.html', {'name': 'Saddam'})
