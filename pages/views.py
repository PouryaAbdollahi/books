from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.


class HomePageView(ListView):
    template_name = 'pages/home.html'

    def get_queryset(self):
        pass
