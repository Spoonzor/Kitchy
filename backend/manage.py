#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitchen_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Assurez-vous que Django est installé et disponible sur votre PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)
