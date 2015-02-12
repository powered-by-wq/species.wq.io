define(['leaflet', 'wq/pages', 'wq/locate', 'wq/app', 'wq/map', './config', 'data/templates'],
function(L, pages, locate, app, map ,config, templates) {
L.Icon.Default.imagePath= "/css/lib/images";

localStorage.clear();

app.init(config, templates);
map.init(config.map);

pages.addRoute('reports/new', 's', function(match, ui, params, hash, evt, $page) {
// Create Leaflet map
var m = L.map('report-new-map').setView(config.map.center, config.map.zoom);
map.createBaseMaps().Street.addTo(m);
// Initialize basemaps & location ...

// Configure Locator

var fields = {
    'toggle': $page.find('input[name=mode]'),
    'latitude': $page.find('input[name=latitude]'),
    'longitude': $page.find('input[name=longitude]'),
    'accuracy': $('input[name=accuracy]')
};

var locator = locate.locator(m, fields);
});
app.jqmInit();

});

