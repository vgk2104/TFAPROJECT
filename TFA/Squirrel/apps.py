from django.apps import AppConfig


class SquirrelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Squirrel'


class MapConfig(AppConfig):
    name = 'map'
