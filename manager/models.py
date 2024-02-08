from django.db import models
from django.utils.timezone import now


class SiteSettings(models.Model):
    """
    Настройки сайта
    """
    site_name = models.CharField(max_length=250, default='Site', null=True, blank=True, verbose_name='Сайт')

    user_name = models.CharField(max_length=250, default='admin', null=True, blank=True, verbose_name='Пользователь')
    user_pass = models.CharField(max_length=250, default='admin', null=True, blank=True, verbose_name='Пароль')
    token = models.CharField(max_length=250, default='Token ', null=True, blank=True, verbose_name='Токен')

    project_name = models.CharField(max_length=250, default=' ', null=True, blank=True, verbose_name='Имя проекта')
    domain_name = models.CharField(max_length=250, default=' ', null=True, blank=True, verbose_name='Домен')
    region = models.TextField(default=' ', null=True, blank=True, verbose_name='Регион')

    document_head = models.TextField(default=' ', null=True, blank=True, verbose_name='Блок head')
    document_body = models.TextField(default=' ', null=True, blank=True, verbose_name='Блок body')
    document_footer = models.TextField(default=' ', null=True, blank=True, verbose_name='Блок footer')

    main_page_title = models.TextField(default=' ', null=True, blank=True, verbose_name='Title')
    main_page_description = models.TextField(default=' ', null=True, blank=True, verbose_name='Description')
    main_page_canonical = models.CharField(max_length=250, default=' ', null=True, blank=True, verbose_name='Canonical')

    contacts_address = models.CharField(max_length=250, default=' ', null=True, blank=True, verbose_name='Адрес')
    contacts_name = models.CharField(max_length=250, default='Стиль потолка', null=True, blank=True, verbose_name='Наименование')
    contacts_tel = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='Телефон')
    contacts_tel_formatted = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='Телефон формат')
    contacts_whatsapp = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='Ватсапп')
    contacts_whatsapp_formatted = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='Ватсапп формат')
    contacts_telegram = models.CharField(max_length=100, default=' ', null=True, blank=True, verbose_name='Телеграм')
    contacts_telegram_formatted = models.CharField(max_length=100, default=' ', null=True, blank=True, verbose_name='Телеграм формат')
    contacts_email = models.CharField(max_length=100, default=' ', null=True, blank=True, verbose_name='E-mail')
    contacts_email_formatted = models.CharField(max_length=100, default=' ', null=True, blank=True, verbose_name='E-mail формат')
    contacts_map = models.TextField(default=' ', null=True, blank=True, verbose_name='Карта ПК-версия')
    contacts_map_mobile = models.TextField(default=' ', null=True, blank=True, verbose_name='Карта мобильная версия')

    requisites_company = models.CharField(max_length=50, default='Стиль потолка', null=True, blank=True, verbose_name='Название компании')
    requisites_inn = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='ИНН')
    requisites_work_hours = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='Часы работы')
    requisites_ogrn = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='ОГРН')
    requisites_bank = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='Банк')
    requisites_bik = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='Бик')
    requisites_count = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='Счет')
    requisites_corr_count = models.CharField(max_length=50, default=' ', null=True, blank=True, verbose_name='Корр. счет')

    time_create = models.CharField(max_length=21, default=now().strftime("%d/%m/%Y - %H:%M:%S"),
                                   verbose_name='time_create', null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'
        ordering = ['-domain_name']
        db_table = 'project'

    def __str__(self):
        return f'Пользователь {self.user_name}, сайт {self.site_name}'
