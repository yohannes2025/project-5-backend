from django.apps import AppConfig


class ProductivityAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productivity_app'

    def ready(self):
        import productivity_app.models
