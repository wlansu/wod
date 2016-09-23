web: gunicorn config.wsgi:application
worker: celery worker --app=wod.taskapp --loglevel=info
