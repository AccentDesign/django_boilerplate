#!/bin/bash

export PGPASSWORD=$RDS_PASSWORD

while ! psql --host=$RDS_HOSTNAME --port=$RDS_PORT --username=$RDS_USERNAME > /dev/null 2>&1; do
    echo 'Waiting for connection with db...'
    sleep 1;
done;
echo 'Connected to db...';

python manage.py migrate
python manage.py runserver 0.0.0.0:8000