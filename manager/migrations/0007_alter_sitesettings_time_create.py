# Generated by Django 4.1 on 2024-04-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_alter_sitesettings_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='time_create',
            field=models.CharField(blank=True, default='12/04/2024 - 13:21:06', max_length=21, null=True, verbose_name='time_create'),
        ),
    ]