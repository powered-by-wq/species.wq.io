from wq.db.rest import app
from wq.db.patterns import rest as patterns
from .models import Report, Species
from .views import ReportViewSet


app.router.register_model(
    Species,
    serializer=patterns.IdentifiedModelSerializer
)
app.router.register_model(Report, viewset=ReportViewSet)
app.router.add_page('index', {'url': ''})
