# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wq.db.contrib.files.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('files', '0001_initial'),
        ('reports', '0004_auto_20150523_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('file', wq.db.contrib.files.models.FileField(upload_to='.', height_field='height', width_field='width')),
                ('size', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField(db_index=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('type', models.ForeignKey(blank=True, to='files.FileType', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
