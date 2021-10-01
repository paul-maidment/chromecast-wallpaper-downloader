SHELL := /bin/bash

.PHONY : venv-setup run

venv-setup:
	python3 -m venv env && source env/bin/activate && pip install --upgrade pip -r requirements.txt
run:
	make venv-setup
	source env/bin/activate && python main.py
