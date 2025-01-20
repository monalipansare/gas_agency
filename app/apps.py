from django.apps import AppConfig
# apps.py
def ready(self):
    import app.signals

class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

