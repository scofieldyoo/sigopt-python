.PHONY: pytest lint

test:	export PYTHONPATH=.
test:
	@python -m pytest -rw -v test

lint:
	@./lint
