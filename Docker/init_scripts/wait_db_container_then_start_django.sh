#!/bin/bash

echo "waiting mysql initialization..."
sleep 12
echo "done waiting... hope it was enough!   "

python ./manage.py migrate
python ./manage.py runserver 0.0.0.0:8000