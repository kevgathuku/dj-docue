web: gunicorn react_django.wsgi --limit-request-line 8188 --log-file -
worker: celery worker --app=react_django --loglevel=info
