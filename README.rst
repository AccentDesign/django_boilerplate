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

Copy the file ``app/local_settings.local`` to ``app/local_settings.py``
In here you can define your own settings.


3, Docker & Python

Build the container::

    docker-compose build

Run python migrations::

    docker-compose run app python manage.py migrate

Create yourself a superuser::

    docker-compose run app python manage.py createsuperuser --email=admin@example.com --first_name=Admin --last_name=User

Up the container::

    docker-compose up


Ready!!
*******

The container is ready at http://127.0.0.1:8000/ and a mail server ready at http://127.0.0.1:1080/


Styling
*******

1, You will need node js installed, please see online for setup

2, To make any style tweaks you will need to install all project dependencies like so::

    npm install

you will propably need gulp and gulp-cli as global dependencies::

    npm install -g gulp gulp-cli

3, ``static/src`` is where you set up your styles, ``static/src/boobstrap/_variables.scss`` are the boorstrap variables used.

4, the ``gulpfile.js`` has a list of tasks to run, to get you started running just gulp will build, compress and repopulate
the ``static/dist`` folder::

    gulp

    eg:

    [09:43:21] Starting 'style_css'...
    [09:43:21] Starting 'fa_css'...
    [09:43:21] Finished 'fa_css' after 34 ms
    [09:43:21] Finished 'style_css' after 107 ms
    [09:43:21] Finished 'bootstrap_css' after 605 ms
    [09:43:21] Starting 'default'...
    [09:43:21] Starting 'bootstrap_compress'...
    [09:43:21] Starting 'bootstrap_fonts'...
    [09:43:21] Starting 'bootstrap_js'...
    [09:43:21] Starting 'style_compress'...
    [09:43:21] Starting 'fa_fonts'...
    [09:43:21] Starting 'jquery'...
    [09:43:21] Finished 'bootstrap_compress' after 257 ms
    [09:43:21] Finished 'style_compress' after 229 ms
    [09:43:21] Finished 'bootstrap_js' after 235 ms
    [09:43:21] Finished 'jquery' after 232 ms
    [09:43:21] Finished 'bootstrap_fonts' after 237 ms
    [09:43:21] Finished 'fa_fonts' after 240 ms
    [09:43:21] Finished 'default' after 271 ms



