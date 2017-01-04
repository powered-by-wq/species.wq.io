from wq.db import rest
from .maps import basemaps, index_map
from django.conf import settings


rest.router.add_page('index', {
    'url': '',
    'map': index_map,
})

rest.router.set_extra_config(
    debug=settings.DEBUG,
    map={
        'bounds': [[-70, -180], [70, 180]],
        'basemaps': basemaps
    },
)
