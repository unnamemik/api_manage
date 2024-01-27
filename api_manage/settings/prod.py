import os

from api_manage.settings.base import BASE_DIR

ALLOWED_HOSTS = ['megaseller.ru',
                 'www.megaseller.ru',
                 'aprelevka.megaseller.ru',
                 'balashiha.megaseller.ru',
                 'bronnitsy.megaseller.ru',
                 'chehov.megaseller.ru',
                 'chernogolovka.megaseller.ru',
                 'dmitrov.megaseller.ru',
                 'dolgoprudnyj.megaseller.ru',
                 'domodedovo.megaseller.ru',
                 'dubna.megaseller.ru',
                 'dzerzhinskij.megaseller.ru',
                 'egorevsk.megaseller.ru',
                 'elektrougli.megaseller.ru',
                 'himki.megaseller.ru',
                 'hotkovo.megaseller.ru',
                 'istra.megaseller.ru',
                 'ivanteevka.megaseller.ru',
                 'kashira.megaseller.ru',
                 'klimovsk.megaseller.ru',
                 'klin.megaseller.ru',
                 'kolomna.megaseller.ru',
                 'krasnoarmejsk.megaseller.ru',
                 'krasnogorsk.megaseller.ru',
                 'krasnoznamensk.megaseller.ru',
                 'kubinka.megaseller.ru',
                 'likino-dulevo.megaseller.ru',
                 'lobnya.megaseller.ru',
                 'lotoshino.megaseller.ru',
                 'luhovicy.megaseller.ru',
                 'lytkarino.megaseller.ru',
                 'lyubercy.megaseller.ru',
                 'mihnevo.megaseller.ru',
                 'mozhajsk.megaseller.ru',
                 'mytishchi.megaseller.ru',
                 'naro-fominsk.megaseller.ru',
                 'noginsk.megaseller.ru',
                 'cheboksary.megaseller.ru',
                 'dedovsk.megaseller.ru',
                 'elektrogorsk.megaseller.ru',
                 'elektrostal.megaseller.ru',
                 'fryanovo.megaseller.ru',
                 'fryazevo.megaseller.ru',
                 'fryazino.megaseller.ru',
                 'kazan.megaseller.ru',
                 'kolchugino.megaseller.ru',
                 'korolev.megaseller.ru',
                 'krasnozavodsk.megaseller.ru',
                 'kurovskoe.megaseller.ru',
                 'losino-petrov.megaseller.ru',
                 'monino.megaseller.ru',
                 'nahabino.megaseller.ru',
                 'nizhny-novgorod.megaseller.ru',
                 'odincovo.megaseller.ru',
                 'orekhovo-zuevo.megaseller.ru',
                 'ozery.megaseller.ru',
                 'ozherelie.megaseller.ru',
                 'pavlovskij-posad.megaseller.ru',
                 'peresvet.megaseller.ru',
                 'podolsk.megaseller.ru',
                 'protvino.megaseller.ru',
                 'pushkino.megaseller.ru',
                 'ramenskoe.megaseller.ru',
                 'reutov.megaseller.ru',
                 'roshal.megaseller.ru',
                 'ruza.megaseller.ru',
                 'saint-petersburg.megaseller.ru',
                 'samara.megaseller.ru',
                 'schelkovo.megaseller.ru',
                 'scherbinka.megaseller.ru',
                 'serebryannye-prudy.megaseller.ru',
                 'sergiev-posad.megaseller.ru',
                 'serpuhov.megaseller.ru',
                 'shahovskoe.megaseller.ru',
                 'shatura.megaseller.ru',
                 'shodnya.megaseller.ru',
                 'sofrino.megaseller.ru',
                 'solnechnogorsk.megaseller.ru',
                 'staraya-kupavna.megaseller.ru',
                 'stupino.megaseller.ru',
                 'taldom.megaseller.ru',
                 'troick.megaseller.ru',
                 'tuchkovo.megaseller.ru',
                 'vidnoe.megaseller.ru',
                 'volokolamsk.megaseller.ru',
                 'voskresensk.megaseller.ru',
                 'yahroma.megaseller.ru',
                 'zaraysk.megaseller.ru',
                 'zelenograd.megaseller.ru',
                 'zheleznodorogny.megaseller.ru',
                 'zhukovskij.megaseller.ru',
                 'zvenigorod.megaseller.ru',
                 ]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'mail.hosting.reg.ru'
EMAIL_HOST_USER = 'info@megaseller.ru'
EMAIL_HOST_PASSWORD = '________________'
EMAIL_PORT = 587

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

BASE_URL = 'http://megaseller.ru/'
