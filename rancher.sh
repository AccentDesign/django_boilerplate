#!/bin/bash

pip install -r requirements.txt
python manage.py collectstatic --noinput

echo "waiting for db..."
while ! nc -w 1 -z $RDS_HOSTNAME $RDS_PORT 2>/dev/null;
do
  echo -n .
  sleep 1
done
echo "db ready..."

echo "app sleeping for 10 seconds to ensure database is accepting commands before migrating..."
sleep 10

python manage.py migrate
gunicorn app.wsgi:application -w 2 -b :8000