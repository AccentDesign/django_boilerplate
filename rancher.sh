#!/bin/bash

export PGPASSWORD=$RDS_PASSWORD

while ! psql --host=$RDS_HOSTNAME --port=$RDS_PORT --username=$RDS_USERNAME > /dev/null 2>&1; do
    echo 'Waiting for connection with db...'
    sleep 1;
done;
echo 'Connected to db...';

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn app.wsgi:application -w 2 -b :8000