from django.apps import AppConfig
import project_x.celery

class DataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Data'


    def ready(self):
        import Data.views