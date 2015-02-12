# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_report_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='longtitude',
            new_name='longitude',
        ),
    ]
