# Generated by Django 3.1.2 on 2020-11-22 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inference', '0005_auto_20201121_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='path',
            field=models.FilePathField(default='/Users/khangtu/PycharmProjects/spam/media', path='/Users/khangtu/PycharmProjects/spam/media'),
        ),
    ]