#!/bin/sh -e

set -e


echo "🛠️ Running migrations..."
uv run python manage.py migrate

echo "🚀 Starting server..."
uv run gunicorn config.wsgi:application --bind 0.0.0.0:8000

exec "$@"
