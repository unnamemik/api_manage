# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, '/var/www/u2139094/data/www/izi-start.ru/api_manage/settings')
sys.path.insert(1, '/var/www/u2139094/data/djenv4.1/lib/python3.10/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'api_manage.settings.base'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()