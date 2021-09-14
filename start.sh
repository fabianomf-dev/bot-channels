#!/bin/bash
source venv/bin/activate
export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_APP=telegram.py
flask run
