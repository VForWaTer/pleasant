# from django.views.generic import TemplateView

from django.conf.urls import url, include
from . import views

app_name = 'base_app'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
#     url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^clear/(?P<pk>\d+)/delete/$', views.delete_data, name='delete_data'),
#     url(r'^data-access/$', views.DataUploadView.as_view(), name='data_access'),

#    url(r'^$', views.HomeView.remove_data.as_view(), name='remove'),
    url(r'^login$', views.Login.as_view(), {'template_name': 'base_app/login.html'}, name='login'),
]


