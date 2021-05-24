#!/bin/sh

chmod +x app/entrypoint.shpython manage.py flush --no-input
python manage.py migrate

exec "$@"
