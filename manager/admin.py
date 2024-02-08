import json
import requests
from django.contrib import admin
from django.utils.timezone import now

from .models import SiteSettings


@admin.action(description='Деактивировать')
def deactivate(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.action(description='Активировать')
def activate(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.action(description='Копировать')
def copy_item(modeladmin, request, queryset):
    for item in queryset:
        item.pk = None
        item.time_create = now().strftime("%d/%m/%Y - %H:%M:%S")
        item.save()


@admin.action(description='Отправить настройки на сайт')
def site_update(modeladmin, request, queryset):
    for site in queryset:
        site_settings = SiteSettings.objects.filter(pk=site.pk).first()
        url_auth = f'https://{site_settings.domain_name}/rest_api/'

        token = site_settings.token
        data = {
            "project_name": site_settings.project_name,
            "domain_name": site_settings.domain_name,
            "region": site_settings.region.split(),
            "document_": {
                "head": site_settings.document_head,
                "body": site_settings.document_body,
                "footer": site_settings.document_footer
            },
            "main_page_": {
                "title": site_settings.main_page_title,
                "description": site_settings.main_page_description,
                "canonical": site_settings.main_page_canonical
            },
            "contacts_": {
                "address": site_settings.contacts_address,
                "name": site_settings.contacts_name,
                "tel": site_settings.contacts_tel,
                "tel_formatted": site_settings.contacts_tel_formatted,
                "whatsapp": site_settings.contacts_whatsapp,
                "whatsapp_formatted": site_settings.contacts_whatsapp_formatted,
                "telegram": site_settings.contacts_telegram,
                "telegram_formatted": site_settings.contacts_telegram_formatted,
                "email": site_settings.contacts_email,
                "email_formatted": site_settings.contacts_email_formatted,
                "map": site_settings.contacts_map,
                "map_mobile": site_settings.contacts_map_mobile
            },
            "requisites_": {
                "company": site_settings.requisites_company,
                "inn": site_settings.requisites_inn,
                "work_hours": site_settings.requisites_work_hours,
                "ogrn": site_settings.requisites_ogrn,
                "bank": site_settings.requisites_bank,
                "bik": site_settings.requisites_bik,
                "count": site_settings.requisites_count,
                "corr_count": site_settings.requisites_corr_count
            }
        }
        data = json.dumps(data)
        cookies = {}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        requests.post(url_auth, data=data, cookies=cookies, headers=headers)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'site_name', 'domain_name', 'contacts_name', 'contacts_tel', 'contacts_address']
    ordering = ['pk']
    search_fields = ['site_name', 'domain_name', 'contacts_name', 'contacts_tel', 'contacts_address']
    list_per_page = 30
    actions = [deactivate, activate, copy_item, site_update]
    fieldsets = (
        (None, {
            'fields': ('site_name',)
        }),
        ('Основное', {
            'fields': (
                'user_name', 'user_pass', 'token', 'project_name', 'domain_name', 'region')
        }),
        ('Поля страниц', {
            'classes': ['collapse in', ],
            'fields': (
                'document_head', 'document_body', 'document_footer')
        }),
        ('Свойства главной страницы', {
            'classes': ['collapse in', ],
            'fields': ('main_page_title', 'main_page_description', 'main_page_canonical')
        }),
        ('Контакты', {
            'classes': ['collapse in', ],
            'fields': (
                'contacts_address', 'contacts_name', 'contacts_tel', 'contacts_tel_formatted', 'contacts_whatsapp',
                'contacts_whatsapp_formatted', 'contacts_telegram', 'contacts_telegram_formatted', 'contacts_email',
                'contacts_email_formatted', 'contacts_map', 'contacts_map_mobile')
        }),
        ('Реквизиты', {
            'classes': ['collapse in', ],
            'fields': (
                'requisites_company', 'requisites_inn', 'requisites_work_hours', 'requisites_ogrn',
                'requisites_bank', 'requisites_bik', 'requisites_count', 'requisites_corr_count',)
        }),
        ('Инфо', {
            'classes': ['collapse in', ],
            'fields': (
                'time_create', 'active')
        }),
    )
    readonly_fields = ["time_create", 'active']
