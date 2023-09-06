web: gunicorn autonomous_dev.wsgi
release: python manage.py migrate --noinput
release: python manage.py collectstatic --noinput