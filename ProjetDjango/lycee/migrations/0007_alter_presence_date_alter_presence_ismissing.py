# Generated by Django 4.0.4 on 2022-05-22 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0006_alter_presence_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 22, 18, 15, 16, 965597), verbose_name='Date of Student Missing'),
        ),
        migrations.AlterField(
            model_name='presence',
            name='isMissing',
            field=models.BooleanField(default=True, help_text='Missing ?', verbose_name='isMissing'),
        ),
    ]
