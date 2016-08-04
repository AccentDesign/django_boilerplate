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
- AWS Elastic Beanstalk basic config

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


Testing
*******

To see the test results and coverage report run::

   docker-compose run app make test

The html coverage report is visible in the browser by looking at the htmlcov/index.html once the tests have run.


Styling
*******

1, You will need node js installed, please see online for setup

2, To make any style tweaks you will need to install all project dependencies like so::

    npm install

you will propably need gulp and gulp-cli as global dependencies::

    npm install -g gulp gulp-cli

3, ``static/scss`` is where you set up your styles, ``static/scss/boobstrap/_boobstrap/_variables.scss`` are the boorstrap variables used.

4, the ``gulpfile.js`` has a list of tasks to run, to get you started running just gulp will build, compress and repopulate
the ``static/dist`` folder::

    gulp

    eg:

    ....
    [09:43:21] Finished 'default' after 271 ms


Deployment on Elastic Beanstalk
*******************************

The file `.ebextensions/01_settings.config` contains a list of all the environment settings required for email, mysql & s3.


The following will setup an elasticbeanstalk environment with no dedicated rds, adjust as required::

2, You will need to install `awsebcli`::

   pip install awsebcli

http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html

3, BEFORE THIS MAKE SURE EVERYTHING IS COMMITTED, run the following commands following the prompts::

   eb init -i
   eb create # optional --db if dedicated rds is required
   eb use <environment-name>
   eb deploy

4, Step 3 will have created a `.elasticbeanstalk/config.yml` which will be ignored in your `.gitignore` file,
please remove these ignored lines as jenkins wont know where to deploy it without them.


Pycharm OSX Interpreter
***********************

Connect SOCAT to docker native::

   brew install socat
   socat TCP-LISTEN:2375,reuseaddr,fork UNIX-CONNECT:/var/run/docker.sock


Pycharm docker API URL:

   tcp://localhost:2375

Leave certificates folder empty.