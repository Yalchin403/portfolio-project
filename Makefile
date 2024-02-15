compile:
	pip-compile --strip-extras --resolver=backtracking requirements.in

install:
	pip-sync requirements.txt
run-local:
	docker compose -f docker-compose-local.yml up --build