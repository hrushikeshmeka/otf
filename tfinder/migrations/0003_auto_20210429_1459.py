# Generated by Django 3.1.3 on 2021-04-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfinder', '0002_auto_20210429_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='des',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Lecturer', 'Lecturer'), ('Asst Prof', 'Asst'), ('Assoc Prof', 'Assoc'), ('Prof', 'Prof')], max_length=20),
        ),
    ]