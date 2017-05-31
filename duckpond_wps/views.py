from django.views.generic import TemplateView


from django.shortcuts import render

# Create your views here.
# Create your views here.
class Workbench(TemplateView):
    template_name = 'duckpond_wps/app_home.html'


class Login(TemplateView):
    template_name = 'base_app/login.html'