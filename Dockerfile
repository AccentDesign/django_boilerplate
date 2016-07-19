FROM        python:3.4.4

WORKDIR     /var/app

COPY        test-requirements.txt /var/app

RUN         pip3 install -r /var/app/test-requirements.txt