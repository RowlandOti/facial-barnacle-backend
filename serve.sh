#!/bin/bash

export FLASK_APP=app.py
/home/pi/.virtualenvs/cv/bin/gunicorn -w 9 app:app