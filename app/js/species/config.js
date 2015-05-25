define(["data/config", "data/templates", "data/version", "module"],
function(config, templates, version, module) {

var overrides = module.config();

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

for (var key in overrides) {
    config[key] = overrides[key];
}

return config;

});
