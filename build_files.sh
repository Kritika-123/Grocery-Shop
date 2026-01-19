#!/bin/bash
echo "BUILD START"

# Install dependencies (do NOT upgrade pip)
python -m pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

echo "BUILD END"
