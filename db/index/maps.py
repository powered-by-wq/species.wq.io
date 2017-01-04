from django.conf import settings

mapbox = "https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}"

attrib = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>'

basemaps = [{
    'name': "Street",
    'type': 'tile',
    'url': mapbox,
    'id': 'mapbox.streets',
    'accessToken': settings.MAPBOX_TOKEN,
    'attribution': attrib,
}, {
    'name': "Terrain",
    'type': 'tile',
    'url': mapbox,
    'id': 'mapbox.outdoors',
    'accessToken': settings.MAPBOX_TOKEN,
    'attribution': attrib,
}, {
    'name': "Aerial",
    'type': 'tile',
    'url': mapbox,
    'id': 'mapbox.satellite',
    'accessToken': settings.MAPBOX_TOKEN,
    'attribution': attrib,
}]


index_map = [{
    'layers': [{
        'name': 'Reports',
        'type': 'geojson',
        'url': 'reports.geojson',
        'popup': 'report',
        'cluster': True,
    }]
}]
