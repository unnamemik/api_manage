from django.db import models
from django.utils.timezone import now


# Create your models here.
class Sensor(models.Model):
    """
    Задача
    """
    STATUS_CHOICES = (
        ('Unset', 'Не определено'),
        ('Alarm!', 'Тревога!'),
        ('Online', 'Онлайн'),
    )
    sensor_name = models.CharField(max_length=500, null=True, blank=True, default=' ', verbose_name='Имя элемента')
    sensor_MAC = models.CharField(max_length=500, null=True, blank=True, default=' ', verbose_name='MAC-адрес датчика')
    sensor_title = models.CharField(max_length=500, default=' ', null=True, blank=True, verbose_name='Датчик')
    sensor_description = models.TextField(default=' ', null=True, blank=True, verbose_name='Описание')
    sensor_email = models.TextField(default=' ', null=True, blank=True, verbose_name='E-mail оповещения')
    sensor_time_create = models.CharField(max_length=21, default=now().strftime("%d/%m/%Y - %H:%M:%S"),
                                          null=True, blank=True, verbose_name='Время создания')
    sensor_status_change = models.CharField(max_length=21, default=now().strftime("%d/%m/%Y - %H:%M:%S"),
                                            null=True, blank=True, verbose_name='Время срабатывания')
    sensor_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unset', verbose_name='Статус')
    sensor_active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['sensor_name']
        db_table = 'sensor'

    def __str__(self):
        return f'{self.sensor_name}'

    def get_summary(self):
        words = self.sensor_description.split()
        return f'{" ".join(words[:20])}...'


class Client(models.Model):
    """
    Информация о клиенте
    """
    client_phone = models.CharField(max_length=18, verbose_name='Телефон', unique=True)
    client_name = models.CharField(max_length=50, verbose_name='Имя', null=True, blank=True, default='Клиент')
    client_info = models.TextField(default=' ', null=True, blank=True, verbose_name='Описание')
    client_email = models.EmailField(max_length=255, verbose_name='Email', null=True, blank=True, default='client@mail.ru')
    client_time_create = models.CharField(max_length=21, default=now().strftime("%d/%m/%Y - %H:%M:%S"),
                                          verbose_name='Дата отправки', null=True, blank=True)
    client_ip_address = models.GenericIPAddressField(verbose_name='IP отправителя', blank=True, null=True, default='127.0.0.1')
    client_active = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-client_time_create']
        db_table = 'client'

    def __str__(self):
        return f'Вам письмо от {self.client_name}, {self.client_phone}'
