#!/bin/bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR=$( dirname "${SCRIPT_DIR}" )

# Start a server in the background
env SASKATOON_TESTING=yes python3 "$PROJECT_DIR/manage.py" runserver 8000 &

testserverpid=$!

# Kill it when the script exits
trap "kill $testserverpid" EXIT

echo "Starting tests in a bit ..."

# Give saskatoon 5 seconds to startup
sleep 5

cd "$PROJECT_DIR"

# Launch the tests
env PYTHONWARNINGS=all \
    PYTHONPATH="${PROJECT_DIR}" \
    DJANGO_SETTINGS_MODULE=saskatoon.settings \
    python3 -m pytest