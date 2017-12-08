#!/bin/sh
set -e

export PGPASSWORD=$RDS_PASSWORD

until psql -h $RDS_HOSTNAME -d $RDS_DB_NAME -p $RDS_PORT -U $RDS_USERNAME -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    python manage.py migrate --noinput
fi

if [ "x$DJANGO_MANAGEPY_COLLECTSTATIC" = 'xon' ]; then
    python manage.py collectstatic --noinput
fi

exec "$@"