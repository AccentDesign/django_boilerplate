#!/usr/bin/env bash
pip install -r test-requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000