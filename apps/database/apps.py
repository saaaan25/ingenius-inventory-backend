from django.apps import AppConfig
import mongoengine
from dotenv import load_dotenv
import os


class DatabaseConfig(AppConfig):
    name = 'apps.database'

    def ready(self):
        try:
            mongoengine.connect(
                db=os.getenv('MONGO_DB_NAME'),
                host=os.getenv('MONGO_HOST'),
                port=int(os.getenv('MONGO_PORT')),
                username=os.getenv('MONGO_USERNAME'),
                password=os.getenv('MONGO_PASSWORD'),
                authentication_source=os.getenv('MONGO_AUTH_SOURCE')
            )
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
        
        import apps.database.signals
