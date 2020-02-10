sh:
	docker-compose run app bash

venv:
	docker-compose run app python -m virtualenv venv

pip: venv
	docker-compose run app ./venv/bin/python -m pip install -r requirements.txt

up:
	docker-compose up -d

notebook:
	docker-compose run -p 8888:8888 app ./venv/bin/python ./manage.py shell_plus --notebook
