# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('photo', models.ImageField(upload_to='', blank=True, null=True)),
                ('latitude', models.FloatField()),
                ('longtitude', models.FloatField()),
                ('accuracy', models.FloatField()),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'species',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='report',
            name='species',
            field=models.ForeignKey(to='reports.Species'),
            preserve_default=True,
        ),
    ]
