web: python manage.py makemigrations
web: python manage.py migrate
web: python manage.py collectstatic --noinput
web: gunicorn T.wsgi --preload --workers 1


