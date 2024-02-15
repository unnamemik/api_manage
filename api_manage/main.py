import json
import requests


def api_set():
    url_auth = 'http://127.0.0.1:8000/rest_api/'

    token = 'Token 01daaa0a7e7e860007a63293c73d8b8f01e0d3c0'
    data = {
        "project_name": "potolki_template",
        "domain_name": "natyajnye-potolki.pro",
        "region_": {
            "what": "Мурманск",
            "where": "Мурманске"
        },
        "document_": {
            "head": "<meta name=\"robots\" content=\"noindex, nofollow\"/>",
            "body": "",
            "footer": ""
        },
        "main_page_": {
            "title": "Установка натяжных потолков под ключ в Мурманске цена за кв. м. - СТИЛЬ ПОТОЛКА",
            "description": "Установка натяжных потолков под ключ в Мурманске цены за кв. м., бесплатный выезд на замер. "
                           "Собственное производство Широкий размер полотна. Монтаж в Мурманске. Заказать качественные "
                           "потолки любой фактуры недорого.",
            "canonical": "https://natyajnye-potolki.pro/"
        },
        "contacts_": {
            "address": "г. Мурманск",
            "name": "Стиль потолка",
            "tel": "+71111113333",
            "tel_formatted": "+7 (111) 111-33-33",
            "whatsapp": "+71111111111",
            "whatsapp_formatted": "",
            "telegram": "+71111111111",
            "telegram_formatted": "",
            "email": "info@natyajnye-potolki.ru",
            "email_formatted": "info@natyajnye-potolki.ru",
            "map": "<script type='text/javascript' charset='utf-8' async src='https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Adcdc78f7b87b715b39893c9db68ec603b916ef5540aeaefba0b154060f5e298d&amp;width=100%25&amp;height=600&amp;lang=ru_RU&amp;scroll=true'></script>",
            "map_mobile": "<script type='text/javascript' charset='utf-8' async src='https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Adcdc78f7b87b715b39893c9db68ec603b916ef5540aeaefba0b154060f5e298d&amp;width=100%25&amp;height=350&amp;lang=ru_RU&amp;scroll=true'></script>"
        },
        "requisites_": {
            "company": "ИП ЗППП",
            "inn": "7711777111",
            "work_hours": "с 10:00 до 19:00",
            "ogrn": "7711777111",
            "bank": "7711777111",
            "bik": "7711777111",
            "count": "7711777111",
            "corr_count": "7711777111"
        }
    }
    data = json.dumps(data)
    cookies = {}
    headers = {'Content-Type': 'application/json', 'Authorization': token}
    response = requests.post(url_auth, data=data, cookies=cookies, headers=headers)
    # print('Response: \n', response.text)


api_set()
