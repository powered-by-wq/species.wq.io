# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_convert_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='photo',
        ),
    ]
