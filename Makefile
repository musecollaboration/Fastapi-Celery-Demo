run:
	poetry run uvicorn app.main:app --reload

celery:
	poetry run celery -A app.tasks worker --loglevel=info -Q low-priority,high-priority