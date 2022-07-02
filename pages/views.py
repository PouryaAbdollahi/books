from django.shortcuts import render
from django.views.generic import ListView, TemplateView


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/about.html'
