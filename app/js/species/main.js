define(['jquery', 'leaflet', 'wq/app', 'wq/map', 'wq/router',
        'wq/locate', 'wq/photos', './config'],
function($, L, app, map, router, locate, photos, config) {

config.presync = function() {
    $('button.sync').html("Syncing...");
};
config.postsync = function(items) {
    $('button.sync').html("Sync Now");
    app.syncRefresh(items);
};

app.use(map);
app.use(photos);
app.init(config).then(function() {
    router.addRoute('reports/new', 's', _locatorMap);
    router.addRoute('outbox/<slug>/edit', 's', _locatorMap);
    app.jqmInit();
    app.prefetchAll();
});

function _locatorMap(match, ui, params, hash, evt, $page) {
    // Create Leaflet map
    var m = L.map('report-new-map').fitBounds(config.map.bounds);
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
}

});

