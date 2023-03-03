ifdef browser
    browser = :
else
	browser = chrome;
endif

ifdef tag
    tag = :
else
	tag = login;
endif


ifdef name
    name = :
else
	name = 1-sign_in;
endif

ifdef folder
    folder = :
else
	folder = access;
endif

by_folder: venv
	$(VENV) behave features/${folder}/ -D browser=chrome

by_name: venv
	$(VENV) behave features/${name}.feature -D browser=chrome

all: venv
	$(VENV) behave -D browser=${browser}

report: venv
	$(VENV) allure serve allure_reports

install: setup activate

dev: venv
	$(VENV) install --dev

no-lock: venv
	$(VENV) install --skip-lock

clean: venv
	$(VENV) --rm

fresh: clean install

lint: venv
	$(VENV) prospector --without-tool pyflakes --without-tool pep257

format: venv
	$(VENV) yapf -i *.py **/*.py **/**/*.py

format-check: venv
	$(VENV) yapf --diff *.py **/*.py **/**/*.py


.DEFAULT_GOAL := help

help:
	cat Makefile

setup:
		 ( \
 			python3 -m venv venv; \
			source venv/bin/activate; \
			pip install -r requirements.txt; \
			pip install --upgrade pip; \
		 )

activate:
		bash --rcfile "venv/bin/activate" -i
