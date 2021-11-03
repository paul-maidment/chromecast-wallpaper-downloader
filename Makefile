SHELL := /bin/bash

.PHONY : venv-setup run

venv-setup:
	python3 -m venv env && source env/bin/activate && pip install --upgrade pip -r requirements.txt
live-download:
	make venv-setup
	source env/bin/activate && python grabber.py
large-live-download:
	make venv-setup
	source env/bin/activate && for ((i=1; i<20; i++)) ; do make live-download; done
run:
	make venv-setup
	source env/bin/activate && python main.py
