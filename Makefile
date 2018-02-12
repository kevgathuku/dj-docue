ARG := $(word 2, $(MAKECMDGOALS) )


clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

test:
	pytest

testreset:
	python manage.py test $(ARG) --parallel
