#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn app.wsgi:application -w 2 -b :8000