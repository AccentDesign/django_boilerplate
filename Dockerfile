FROM        python:3.6

ARG         DEV_MODE

WORKDIR     /code
ADD         . /code

# Install dependencies
RUN         apt-get update && apt-get install -y \
                postgresql-client \
                libpq-dev \
            --no-install-recommends && rm -rf /var/lib/apt/lists/

# Python packages
RUN         if [ "x$DEV_MODE" = 'xon' ] ; then \
            pip install --no-cache-dir -r test-requirements.txt ; else \
            pip install --no-cache-dir -r requirements.txt ; fi

# Expose port
EXPOSE 8000

# Add any custom, static environment variables needed by Django:
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=app.settings \
    SECRET_KEY='***** change me *****' \
    ALLOWED_HOSTS=* \
    RDS_HOSTNAME=db \
    RDS_PORT=5432 \
    RDS_DB_NAME=postgres \
    RDS_USERNAME=postgres \
    RDS_PASSWORD=password \
    EMAIL_HOST=mail \
    EMAIL_PORT=1025 \
    EMAIL_HOST_USER=user \
    EMAIL_HOST_PASSWORD=password

# uWSGI configuration:
ENV UWSGI_WSGI_FILE=app/wsgi.py \
    UWSGI_HTTP=:8000 \
    UWSGI_MASTER=1 \
    UWSGI_WORKERS=2 \
    UWSGI_THREADS=8 \
    UWSGI_UID=1000 \
    UWSGI_GID=2000 \
    UWSGI_LAZY_APPS=1 \
    UWSGI_WSGI_ENV_BEHAVIOR=holy

# Docker entrypoint:
ENV DJANGO_MANAGEPY_MIGRATE=on \
    DJANGO_MANAGEPY_COLLECTSTATIC=on

ENTRYPOINT ["/code/docker-entrypoint.sh"]

# Start uWSGI:
CMD ["uwsgi", "--http-auto-chunked", "--http-keepalive"]