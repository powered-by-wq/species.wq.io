from django.db import models
from wq.db.patterns import models as patterns
from wq.db.contrib.files.models import BaseFileAttachment
from django.contrib.contenttypes.fields import GenericRelation


class Species(patterns.IdentifiedModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "species"


class Photo(BaseFileAttachment):
    pass


class Report(models.Model):
    photos = GenericRelation(Photo)
    date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.FloatField()
    species = models.ForeignKey(Species)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        if not self.id:
            return "New Report"
        return "%s on %s" % (self.species, self.date)

    class Meta:
        ordering = ['-date', '-pk']
