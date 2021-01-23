from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def say_hello(request):
    return render(request, 'home.html', {'var1': 'Hii'})


def greetings(request):
    return HttpResponse('<h1>Welcome to Django</h1>')


def expression(request):
    name1 = request.POST["text1"]
    name2 = request.POST["text2"]
    namvar = name1 + "    " + name2
    return render(request, 'name.html', {'fullname': namvar})
