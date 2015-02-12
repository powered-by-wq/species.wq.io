# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 2, 12, 3, 52, 3, 743885, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
