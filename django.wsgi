import os
import sys

path='/srv/www/htdocs/lb2Contacts'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'lb2Contacts.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
