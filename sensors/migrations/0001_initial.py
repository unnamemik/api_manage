# Generated by Django 5.0.2 on 2024-03-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(blank=True, default=' ', max_length=500, null=True, verbose_name='Имя элемента')),
                ('sensor_MAC', models.CharField(blank=True, default=' ', max_length=500, null=True, verbose_name='MAC-адрес датчика')),
                ('sensor_title', models.CharField(blank=True, default=' ', max_length=500, null=True, verbose_name='Датчик')),
                ('sensor_description', models.TextField(blank=True, default=' ', null=True, verbose_name='Описание')),
                ('sensor_email', models.TextField(blank=True, default=' ', null=True, verbose_name='E-mail оповещения')),
                ('sensor_time_create', models.CharField(blank=True, default='17/03/2024 - 13:57:22', max_length=21, null=True, verbose_name='Время создания')),
                ('sensor_status_change', models.CharField(blank=True, default='17/03/2024 - 13:57:22', max_length=21, null=True, verbose_name='Время срабатывания')),
                ('sensor_status', models.CharField(choices=[('unknown', 'Неопределено'), ('alarm', 'Тревога!'), ('online', 'Онлайн')], default='unknown', max_length=10, verbose_name='Статус')),
                ('sensor_showed', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество показов')),
            ],
            options={
                'verbose_name': 'Датчик',
                'verbose_name_plural': 'Датчики',
                'db_table': 'sensor',
                'ordering': ['sensor_name'],
            },
        ),
    ]
