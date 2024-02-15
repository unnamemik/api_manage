# Generated by Django 4.1 on 2024-02-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_remove_sitesettings_region_sitesettings_region_what_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesettings',
            options={'ordering': ['-domain_name'], 'verbose_name': 'Настройки сайта', 'verbose_name_plural': 'Настройки сайтов'},
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='main_page_description',
            field=models.CharField(blank=True, default=' ', max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='main_page_title',
            field=models.CharField(blank=True, default=' ', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='time_create',
            field=models.CharField(blank=True, default='15/02/2024 - 14:47:38', max_length=21, null=True, verbose_name='time_create'),
        ),
    ]
