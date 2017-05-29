from django.views.generic import TemplateView

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
class HomeView(TemplateView):
    template_name = 'base_app/home.html'


class Login(TemplateView):
    template_name = 'base_app/login.html'
