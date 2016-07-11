.PHONY: test

test:
	flake8
	coverage erase
	coverage run manage.py test
	coverage combine
	coverage html
	coverage report