# Generated by Django 3.1.3 on 2021-05-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfinder', '0016_auto_20210502_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posted',
            name='lev',
        ),
    ]
