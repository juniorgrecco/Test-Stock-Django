from urllib import request
from django.shortcuts import render


def index(request):
    context = {"nome": " "}
    return render(request, "home.html", context)
