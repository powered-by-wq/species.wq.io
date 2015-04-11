from .models import Report
from wq.db.rest.views import ModelViewSet
from rest_framework.permissions import AllowAny


class ReportViewSet(ModelViewSet):
    permission_classes = [AllowAny]
