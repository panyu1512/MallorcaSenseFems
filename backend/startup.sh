#!/usr/bin/env bash
cd /senseFems/app

echo "Using django settings $DJANGO_SETTINGS_MODULE"

echo "Running migrations"
python manage.py migrate --settings=$DJANGO_SETTINGS_MODULE
python manage.py collectstatic --no-input

if [[ $DJANGO_ENVIRONMENT = "development" ]]; then
  echo "Freezing container"
  echo "Run 'python manage.py runserver 0.0.0.0:8000' in another shell to run the development server"
  tail -f /dev/null

else
  N_WORKERS=${GUNICORN_WORKERS:-2}
  N_THREADS=${GUNICORN_THREADS:-4}

  echo "Using $N_WORKERS workers and $N_THREADS threads"

  if [[ $# -ne 0 ]]; then
    ARGS="$@"
  else
    ARGS="--workers=$N_WORKERS --threads=$N_THREADS --worker-class=gthread -b 0.0.0.0:8000"
  fi

  # Uncomment when needed NGINX, nginx must be installed on the container
  # echo "Starting NGINX"
  # nginx

  echo "gunicorn senseFems.wsgi $ARGS"
  gunicorn senseFems.wsgi $ARGS
fi