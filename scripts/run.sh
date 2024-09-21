#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

# celery -A app worker -l info
# python manage.py celery -A app worker -l info -B

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi  

