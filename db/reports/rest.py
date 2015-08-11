from wq.db import rest
from wq.db.patterns import rest as patterns
from .models import Report, Species
from .serializers import ReportSerializer
from .views import ReportViewSet

rest.router.register_model(
    Species,
    serializer=patterns.IdentifiedModelSerializer
)
rest.router.register_model(
    Report,
    serializer=ReportSerializer,
    viewset=ReportViewSet,
    reversed=True
)
rest.router.add_page('index', {'url': ''})
