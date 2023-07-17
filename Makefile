build:
	docker compose -f local.yml up --build -d --remove-orphans

logs:
	docker compose -f local.yml logs

up:
	docker compose -f local.yml up

down:
	docker compose -f local.yml down

backup:
	docker compose -f local.yml exec postgres backup

backups:
	docker compose -f local.yml exec postgres backups