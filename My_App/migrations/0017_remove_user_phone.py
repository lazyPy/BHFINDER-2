# Generated by Django 4.1 on 2022-08-14 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0016_alter_boardinghouse_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]