.PHONY: test

test:
	coverage erase
	coverage run manage.py test
	coverage combine
	coverage html
	coverage report