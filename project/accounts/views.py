from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class SignUpView(CreateView):
    model = User
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    form_class = UserCreationForm