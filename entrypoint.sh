#!/bin/bash
set -e

echo "▶ Running migrations…"
python manage.py migrate --noinput

echo "▶ Collecting static assets…"
python manage.py collectstatic --noinput

echo "▶ Starting Gunicorn…"
exec gunicorn conduit.wsgi:application \
  --bind 0.0.0.0:8000 \
  --worker-class sync \
  --log-file -