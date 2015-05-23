# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20150212_0402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-date', '-pk']},
        ),
        migrations.AlterField(
            model_name='report',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
