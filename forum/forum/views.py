# _*_ encoding:utf-8 _*_
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {

    })