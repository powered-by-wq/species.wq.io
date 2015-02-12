from wq.db.patterns import admin
from .models import Species


admin.site.register(Species, admin.IdentifiedModelAdmin)
