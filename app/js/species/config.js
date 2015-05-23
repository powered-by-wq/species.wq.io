define(["data/config", "data/templates", "data/version"],
function(config, templates, version) {

config.template = {
    'templates': templates,
    'defaults': {
        'version': version
    }
};

config.transitions = {
    'default': "slide",
    'save': "flip"
};

config.map = {
    'bounds': [[44.8, -108], [45.8, -107]]
};

return config;

});
