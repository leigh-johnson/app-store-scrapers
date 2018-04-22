#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A app_store_scrapers.taskapp beat -l INFO
