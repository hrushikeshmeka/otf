# Generated by Django 3.1.3 on 2021-05-02 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfinder', '0017_remove_posted_lev'),
    ]

    operations = [
        migrations.AddField(
            model_name='posted',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Closed', max_length=20, verbose_name='Status'),
        ),
    ]