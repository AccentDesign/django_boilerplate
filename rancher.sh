#!/usr/bin/env bash

echo "waiting for db..."
while ! nc -w 1 -z $RDS_HOSTNAME $RDS_PORT 2>/dev/null;
do
  echo -n .
  sleep 1
done
echo "db ready"

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn app.wsgi:application -w 2 -b :8000