"""
Root-level WSGI entrypoint for Vercel and other deployment platforms.
Vercel looks for an 'app' variable in this file.
"""
import os

# Set production settings BEFORE any Django imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cliniclink.settings.production')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Vercel requires the variable to be named 'app'
app = application
