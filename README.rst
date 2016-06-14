******************
Django Boilerplate
******************

Description
***********

Bare bones starter project complete with the following

- Authentication
- Email Templates
- Login, password reset, password change
- Bootstrap3

Getting Started
***************

1, Clone the repo::

    git clone https://bitbucket.org/accent/django_boilerplate.git

2, You will also need some local settings as the default's are production ready.

Copy the file app/local_settings.local to app/local_settings.py
In here you can define your own settings.


3, The following will build the bootstrap files

Install dependencies::

    npm run bs_inst

Watch less less files and compile them to css::

    npm run bs_watch

Regenerate the dist folder::

    npm run bs_dist

4, Docker & Python

Build the container::

    docker-compose build

Run python migrations::

    docker-compose run app python manage.py migrate

Up the container::

    docker-compose up


Ready!!
*******

The container is ready at http://127.0.0.1:8000/ and a mail server ready at http://127.0.0.1:1080/
