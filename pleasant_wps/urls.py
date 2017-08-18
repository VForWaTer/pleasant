from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from . import views


app_name = 'pleasant_wps'

urlpatterns = [
    url(r'^$', views.Workbench.as_view(), name='workbench'),
    url(r'^login$', views.Login.as_view(), {'template_name': 'base_app/login.html'}, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)