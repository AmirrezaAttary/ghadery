from django.apps import AppConfig


class PazireshConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.paziresh'
    def ready(self):
        import app.paziresh.signals