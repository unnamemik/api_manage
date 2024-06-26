# Generated by Django 4.1 on 2024-03-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_remove_sensor_sensor_showed_sensor_sensor_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_status',
            field=models.CharField(choices=[('Unset', 'Не определено'), ('Alarm!', 'Тревога!'), ('Online', 'Онлайн')], default='Unset', max_length=10, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_status_change',
            field=models.CharField(blank=True, default='20/03/2024 - 14:46:54', max_length=21, null=True, verbose_name='Время срабатывания'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_time_create',
            field=models.CharField(blank=True, default='20/03/2024 - 14:46:54', max_length=21, null=True, verbose_name='Время создания'),
        ),
    ]
