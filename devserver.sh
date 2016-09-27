#!/bin/bash

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
python manage.py runserver 0.0.0.0:8000
