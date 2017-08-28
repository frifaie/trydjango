import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    num = random.randint(0, 100000)
    return render(request, 'base.html', {"html_var": "context var", "num": num})
