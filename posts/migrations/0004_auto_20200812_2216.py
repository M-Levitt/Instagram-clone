# Generated by Django 2.2 on 2020-08-13 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200812_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likeCounter',
        ),
        migrations.AddField(
            model_name='postlike',
            name='likeCounter',
            field=models.SmallIntegerField(default=0),
        ),
    ]