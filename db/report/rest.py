from wq.db import rest
from .models import Report
from .serializers import ReportSerializer
import datetime


def recent_reports(qs, request):
    start_date = datetime.date.today() - datetime.timedelta(days=180)
    return qs.filter(date__gte=start_date)


rest.router.register_model(
    Report,
    serializer=ReportSerializer,
    fields="__all__",
    cache_filter=recent_reports,
    locate=True,
    map=[{
        'mode': 'list',
        'autoLayers': True,
        'layers': [],
    }, {
        'mode': 'detail',
        'autoLayers': True,
        'layers': [],
    }, {
        'mode': 'edit',
        'layers': [{
            'type': 'geojson',
            'name': 'Location',
            'url': 'reports/{{id}}.geojson',
        }],
    }],
)
