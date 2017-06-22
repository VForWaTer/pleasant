from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    name = 'base_app'


class PhotosConfig(AppConfig):
    name = 'mysite.photos'