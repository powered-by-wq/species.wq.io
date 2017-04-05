from wq.db import rest
from .models import Report
from .serializers import ReportSerializer


rest.router.register_model(
    Report,
    serializer=ReportSerializer,
    fields="__all__",
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
