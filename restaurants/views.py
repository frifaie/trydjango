import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    num = random.randint(0, 100000)
    a_list = [num, random.randint(0, 100000), random.randint(0, 100000)]
    context = {"html_var": True, "num": num, "a_list": a_list}
    return render(request, 'home.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)
