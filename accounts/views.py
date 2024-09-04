from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class UserRegistraterForm(UserCreationForm):
    usable_password = None

class SignUpView(CreateView):
    form_class = UserRegistraterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
