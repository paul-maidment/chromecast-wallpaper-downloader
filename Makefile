SHELL := /bin/bash
venv-setup:
	python3 -m venv env && source ./env/bin/activate && pip install -r requirements.txt
