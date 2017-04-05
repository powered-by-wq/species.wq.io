from wq.db import rest
from .models import Species


rest.router.register_model(
    Species,
    lookup="slug",
    fields="__all__",
    cache="all",
)
