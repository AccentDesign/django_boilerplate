FROM        python:3.10-slim

# Build args
ARG         PIPENV_INSTALL_OPTIONS=--deploy

# Install dependencies
RUN         set -ex \
            && apt-get update \
            && apt-get install -y \
                gcc \
                libjpeg62 \
                libjpeg62-turbo-dev \
                libpq-dev \
            --no-install-recommends \
            && rm -rf /var/lib/apt/lists/

# Install pipenv and compilation dependencies
RUN         pip install pipenv

# Install python dependencies in /.venv
COPY        Pipfile* /
ARG         PIPENV_INSTALL_OPTIONS
RUN         PIPENV_VENV_IN_PROJECT=1 pipenv install $PIPENV_INSTALL_OPTIONS

# Set the path to the virtualenv
ENV         PATH="/.venv/bin:$PATH"

# Copy your application code to the container
RUN         mkdir /code/
WORKDIR     /code/
ADD         . /code/

# Add any custom, static environment variables needed by Django:
ENV         PYTHONUNBUFFERED=1 \
            PYTHONDONTWRITEBYTECODE=1 \
            DJANGO_SETTINGS_MODULE=app.settings \
            SECRET_KEY='***** change me *****' \
            ALLOWED_HOSTS=* \
            CSRF_TRUSTED_ORIGINS=http://localhost:8000 \
            RDS_HOSTNAME=db \
            RDS_PORT=5432 \
            RDS_DB_NAME=postgres \
            RDS_USERNAME=postgres \
            RDS_PASSWORD=password \
            EMAIL_HOST=mail \
            EMAIL_PORT=1025 \
            EMAIL_HOST_USER=user \
            EMAIL_HOST_PASSWORD=password

# Docker entrypoint:
ENV         DJANGO_MANAGEPY_MIGRATE=on \
            DJANGO_MANAGEPY_COLLECTSTATIC=on

ENTRYPOINT  ["/code/docker-entrypoint.sh"]

# Start uWSGI:
CMD         ["uwsgi", "--ini", "uwsgi.ini"]