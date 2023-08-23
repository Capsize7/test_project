# Django 3.2 Test task about service to check .py files

This is my test task project. It is the service which check your '.py' file by pylint to detect some errors and flaws in the code. You will be noticed by e-mail which include log about your checking files.
There is a celery task with celery-beat to set up the schedule for checking files and sending report. This project will be updating in nearest future.
 
## Features
- Python
- Django
- PostgreSQL
- NGINX
- Gunicorn
- Docker
- Celery
- Celery-beat
- Redis

## How to install
```
1)Clone the project:
- git clone https://github.com/Capsize7/test_project           

2)Run the dockers images
- docker-compose -f docker-compose.prod.yml up -d --build

3)Apply migrations for db
- docker-compose -f docker-compose.prod.yml exec web-app python manage.py migrate --noinput

4)Collect the static files
- docker-compose -f docker-compose.prod.yml exec web-app python manage.py collectstatic --no-input
```

## License

The MIT License (MIT)
