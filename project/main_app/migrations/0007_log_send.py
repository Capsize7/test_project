# Generated by Django 3.2.16 on 2023-08-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20230819_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='send',
            field=models.BooleanField(default=False),
        ),
    ]
