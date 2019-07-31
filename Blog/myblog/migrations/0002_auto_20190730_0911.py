# Generated by Django 2.2.3 on 2019-07-30 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auther',
            name='email',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='myblog',
            name='bdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 30, 9, 11, 23, 211510, tzinfo=utc), null=True),
        ),
    ]
