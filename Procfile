web: gunicorn autonomous_dev.wsgi
release: python manage.py migrate --noinput \
    python manage.py collectstatic --noinput