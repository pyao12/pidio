#!/bin/bash

python manage.py migrate
python csuh.py
waitress-serve --listen=0.0.0.0:8000 pidio.wsgi:application