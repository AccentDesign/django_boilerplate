******************
Django Boilerplate
******************

|Build_Status| |Coverage_Status|

.. |Build_Status| image:: https://circleci.com/gh/AccentDesign/django_boilerplate.svg?style=svg
   :target: https://circleci.com/gh/AccentDesign/django_boilerplate
.. |Coverage_Status| image:: http://img.shields.io/coveralls/AccentDesign/django_boilerplate/master.svg
   :target: https://coveralls.io/r/AccentDesign/django_boilerplate?branch=master

Description
***********

Bare bones starter project complete with the following

- Email authentication
- Login, password reset, password change
- Bootstrap3

Getting Started
***************

1, Clone the repo::

    git clone https://github.com/AccentDesign/django_boilerplate.git

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

The container is ready at http://<docker host ip>:8000/ and a mail server ready at http://<docker host ip>:1080/


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

    ....
    [09:43:21] Finished 'default' after 271 ms



