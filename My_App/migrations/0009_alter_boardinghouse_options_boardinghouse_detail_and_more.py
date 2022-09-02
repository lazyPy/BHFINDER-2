# Generated by Django 4.1 on 2022-08-14 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0008_boardinghouse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boardinghouse',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='boardinghouse',
            name='detail',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boardinghouse',
            name='phone',
            field=models.IntegerField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boardinghouse',
            name='picture',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(max_length=200, verbose_name='Contact Number'),
        ),
    ]