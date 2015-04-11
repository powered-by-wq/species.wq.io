from django.db import models
from wq.db.patterns import models as patterns


class Species(patterns.IdentifiedModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "species"


class Report(models.Model):
    photo = models.ImageField(null=True, blank=True)
    date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.FloatField()
    species = models.ForeignKey(Species)
    notes = models.TextField()

    def __str__(self):
        if not self.id:
            return "New Report"
        return "%s on %s" % (self.species, self.date)
