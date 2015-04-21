from wq.db import rest
from wq.db.patterns import rest as patterns
from .models import Report, Species
from .views import ReportViewSet


rest.router.register_model(
    Species,
    serializer=patterns.IdentifiedModelSerializer
)
rest.router.register_model(Report, viewset=ReportViewSet)
rest.router.add_page('index', {'url': ''})
