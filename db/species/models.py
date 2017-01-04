from django.db import models
import pystache


class Species(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
    )
    slug = models.CharField(
        max_length=50,
        verbose_name="URL Slug",
    )

    wq_label_template = "{{name}}"

    def __str__(self):
        return pystache.render(self.wq_label_template, self)

    class Meta:
        verbose_name = "species"
        verbose_name_plural = "species"
