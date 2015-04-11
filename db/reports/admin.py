from django.contrib import admin
from wq.db.patterns import admin as patterns
from .models import Species


admin.site.register(Species, patterns.IdentifiedModelAdmin)
