from api_manage.settings.base import BASE_DIR

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / 'static/'  # for local dev, off on web
]

MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = "/media/"

BASE_URL = 'localhost'
