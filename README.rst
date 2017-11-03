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
- Karma CSS

Getting Started
***************

1, Clone the repo::

    git clone https://github.com/AccentDesign/django_boilerplate.git


2, Docker & Python

Build the container::

    docker-compose build

Up the container, this will also run migrations for you::

    docker-compose up

Create yourself a superuser::

    docker exec -it <container_name> bash
    python manage.py createsuperuser --email=admin@example.com --first_name=Admin --last_name=User


Run python migrations manually::

    docker exec -it <container_name> bash
    python manage.py migrate


Ready!!
*******

The container is ready at http://<docker host ip>:8000/ and a mail server ready at http://<docker host ip>:1080/


Testing
*******

To see the test results and coverage report run::

   docker exec -it <container_name> bash
   make test

The html coverage report is visible in the browser by looking at the htmlcov/index.html once the tests have run.
