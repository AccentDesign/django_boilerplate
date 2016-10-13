#!/bin/bash

export PGPASSWORD=$RDS_PASSWORD

while ! psql -h $RDS_HOSTNAME -d $RDS_DB_NAME -p $RDS_PORT -U $RDS_USERNAME -c "SELECT version();" > /dev/null 2>&1; do
    echo 'Waiting for connection with db...'
    sleep 1;
done;
echo 'Connected to db...';

python manage.py migrate
python manage.py runserver 0.0.0.0:8000