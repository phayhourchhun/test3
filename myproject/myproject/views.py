# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello Crush, Welcome to the homepage!")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is the about page. Here you can learn more about us.")
    return render(request, 'about.html')

