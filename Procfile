web: gunicorn config.wsgi:application
worker: celery worker --app=wod_new.taskapp --loglevel=info
