#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KBN1.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
>>>>>>> f40088e11f6ed6131d4291bf34da929df623c766

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
