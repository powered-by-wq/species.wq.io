from django.contrib.gis.db import models
import pystache


class Report(models.Model):
    species = models.ForeignKey(
        "species.Species",
        verbose_name="Species",
    )
    date = models.DateField(
        verbose_name="Date",
    )
    toggle = models.CharField(
        choices=(
            ("gps", "Use GPS"),
            ("interactive", "Point on Map"),
            ("manual", "Enter Manually"),
        ),
        max_length=11,
        null=True,
        blank=True,
        verbose_name="Location Mode",
    )
    geometry = models.PointField(
        srid=4326,
        verbose_name="Location",
    )
    latitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Latitude",
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Longitude",
    )
    accuracy = models.FloatField(
        null=True,
        blank=True,
        verbose_name="GPS Accuracy",
    )
    notes = models.TextField(
        null=True,
        blank=True,
        verbose_name="Notes",
    )

    wq_label_template = "{{species.name}} on {{date}}"

    def __str__(self):
        return pystache.render(self.wq_label_template, self)

    class Meta:
        verbose_name = "report"
        verbose_name_plural = "reports"
        ordering = ("-date",)


class Photo(models.Model):
    report = models.ForeignKey(
        Report,
        related_name="photos",
    )
    file = models.ImageField(
        upload_to="reports",
        null=True,
        blank=True,
        verbose_name="Photo",
    )

    def __label__(self):
        return self.file and self.file.name

    class Meta:
        verbose_name = "photo"
        verbose_name_plural = "photos"
