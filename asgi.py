# Root-level ASGI entrypoint for deployment platforms
# This re-exports the application from cliniclink/asgi.py

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cliniclink.settings.production')

from cliniclink.asgi import application  # noqa: F401
