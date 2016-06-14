FROM        python:3.4.4

WORKDIR     /var/app

COPY        requirements.txt /var/app

RUN         pip3 install -r /var/app/requirements.txt