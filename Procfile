web: newrelic-admin run-program uwsgi uwsgi.ini
worker: celery -A gehealthcare worker -l info --concurrency=2 -B
