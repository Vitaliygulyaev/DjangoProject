from django.shortcuts import render
from django.http import HttpResponse
from .models import objects
from .forms import log_in


# Create your views here.

# def login(request):
#     return render(request, 'login.html')


def index(request):
    return render


def login(request):
    form = log_in()
    return render('login.html', {'form': form})