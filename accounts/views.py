from django.shortcuts import render
from django.http import HttpResponse

def display_login(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
