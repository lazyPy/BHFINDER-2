# Generated by Django 4.1 on 2022-08-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0027_alter_boardinghouse_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardinghouse',
            name='picture',
            field=models.ImageField(default=1, upload_to='bh-images/'),
            preserve_default=False,
        ),
    ]