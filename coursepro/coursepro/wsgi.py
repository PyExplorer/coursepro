import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursepro.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'LocalSettings')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
