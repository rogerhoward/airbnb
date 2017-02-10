#!/usr/bin/env bash

dtstamp=$(date +%Y%m%d_%H%M%S)
. ~/.virtualenvs/airbnb/bin/activate

git pull
./airbnb.py
git add -A
git commit -m "$dtstamp"
git push

deactivate