from django.conf.urls import url, include
from . import views


app_name = 'duckpond_wps'

urlpatterns = [
    url(r'^$', views.Workbench.as_view(), name='workbench'),
    url(r'^login$', views.Login.as_view(), {'template_name': 'base_app/login.html'}, name='login'),
]
