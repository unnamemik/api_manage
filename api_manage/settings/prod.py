import os

from api_manage.settings.base import BASE_DIR

ALLOWED_HOSTS = ['izi-start.ru',
                 'www.izi-start.ru',
                 ]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'mail.hosting.reg.ru'
EMAIL_HOST_USER = 'api@izi-start.ru'
EMAIL_HOST_PASSWORD = 'qB1rN1eM0wyL1pO4'
EMAIL_PORT = 587

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

BASE_URL = 'localhost'
