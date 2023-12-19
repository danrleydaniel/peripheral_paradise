import os
from django.core.wsgi import get_wsgi_application
from mutpy import commandline

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "peripheral_paradise.settings")
get_wsgi_application()

if __name__ == "__main__":
    mutation_config = {
        'target': 'meu_app',
        'unit_test': 'meu_app.tests',
        'runner': 'python',
        'disable_operator': 'config',
    }

    commandline.main(mutation_config)
