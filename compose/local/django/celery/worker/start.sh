#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A app_store_scrapers.taskapp worker -l INFO
