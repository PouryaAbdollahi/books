from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from django.views.generic import CreateView
# Create your views here.


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('pages:home')
    template_name = 'registration/signup.html'

