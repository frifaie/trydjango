import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = random.randint(0, 100000)
        a_list = [num, random.randint(0, 100000), random.randint(0, 100000)]
        context = {"html_var": True, "num": num, "a_list": a_list}
        return context
