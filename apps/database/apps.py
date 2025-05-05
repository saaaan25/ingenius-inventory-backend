from django.apps import AppConfig
import mongoengine


class DatabaseConfig(AppConfig):
    name = 'apps.database'

    def ready(self):
        mongoengine.connect(
            db='ingenius_inventory_nsql',
            host='localhost',
            port=27017,
            username='basedatos2',
            password='base_datos_2',
            authentication_source='admin'
        )
