FROM        accent/python-uwsgi-nginx:3.10

# Build args
ARG         PIPENV_INSTALL_OPTIONS=--deploy

# Copy your application code to the container
COPY         . /app/

# Install pipenv and compilation dependencies
RUN         pip install pipenv

# Generate the Pipfile.lock during the image build process, then immediately remove the venv.
# only needed if no Pipfile.lock exists
# RUN         pipenv lock && pipenv --clear && pipenv --rm

# Install python dependencies
ARG         PIPENV_INSTALL_OPTIONS
RUN         pipenv install --system $PIPENV_INSTALL_OPTIONS

# Add any custom, static environment variables needed by Django:
ENV         NGINX_CONTENT_ROOT=/app/public \
            PYTHONUNBUFFERED=1 \
            PYTHONDONTWRITEBYTECODE=1 \
            DJANGO_SETTINGS_MODULE=app.settings \
            SECRET_KEY='***** change me *****' \
            ALLOWED_HOSTS=* \
            CSRF_TRUSTED_ORIGINS=http://localhost \
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
