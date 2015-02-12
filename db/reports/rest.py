from wq.db.rest import app
from .models import Report, Species
from .views import ReportViewSet


app.router.register_model(Species)
app.router.register_model(Report, viewset=ReportViewSet)
app.router.add_page('index', {'url': ''})
