.PHONY: test

test:
	flake8
	coverage erase
	DJANGO_SETTINGS_MODULE=tests.settings PYTHONPATH=. coverage run manage.py test
	coverage combine
	coverage html
	coverage report