#!/bin/bash
source venv/bin/activate

exec gunicorn -b 0.0.0.0:5000 -w 4 --access-logfile - --error-logfile - app.app:app