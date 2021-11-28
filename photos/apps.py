from django.apps import AppConfig


class PhotosConfig(AppConfig):
    name = 'photos'
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'