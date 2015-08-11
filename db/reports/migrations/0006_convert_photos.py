# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def update_photos(apps, schema_editor):
    Photo = apps.get_model("reports", "Photo")
    Report = apps.get_model("reports", "Report")
    ContentType = apps.get_model("contenttypes", "ContentType")
    ct = ContentType.objects.get_for_model(Report)
    for report in Report.objects.all():
        if not report.photo:
            continue
        Photo.objects.create(
            name=report.photo.name.split('/')[-1],
            file=report.photo,
            content_type=ct,
            object_id=report.pk,
        )


def remove_photos(apps, schema_editor):
    Photo = apps.get_model("reports", "Photo")
    Photo.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_photo'),
    ]

    operations = [
        migrations.RunPython(update_photos, remove_photos),
    ]
