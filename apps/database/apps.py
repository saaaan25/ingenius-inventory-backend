from django.apps import AppConfig
import mongoengine
from dotenv import load_dotenv
import os


class DatabaseConfig(AppConfig):
    name = 'apps.database'

    def ready(self):
        mongoengine.connect(
            db=os.getenv('MONGO_DB_NAME'),
            host=os.getenv('MONGO_HOST'),
            port=int(os.getenv('MONGO_PORT')),
            username=os.getenv('MONGO_USERNAME'),
            password=os.getenv('MONGO_PASSWORD'),
            authentication_source=os.getenv('MONGO_AUTH_SOURCE')
        )
