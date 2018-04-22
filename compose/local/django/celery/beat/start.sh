#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


rm -f './celerybeat.pid'
celery -A app_store_scrapers.taskapp beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
