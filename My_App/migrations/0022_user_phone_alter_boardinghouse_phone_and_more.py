# Generated by Django 4.1 on 2022-08-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0021_alter_boardinghouse_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=1, max_length=200, verbose_name='Contact Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boardinghouse',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='boardinghouse',
            name='picture',
            field=models.ImageField(upload_to='bh-images/'),
        ),
    ]
