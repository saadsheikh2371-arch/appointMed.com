#!/bin/bash
# Vercel build script for Django

echo "==> Installing Python dependencies..."
pip install -r requirements.txt

echo "==> Collecting static files..."
python manage.py collectstatic --noinput --settings=cliniclink.settings.production

echo "==> Build complete."
