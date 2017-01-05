define(["data/config", "data/templates", "data/version", "module"],
function(config, templates, version, module) {

var overrides = module.config();

config.router = {
    'base_url': ''
};

config.template = {
    'templates': templates,
    'defaults': {
        'version': version,
        'first_photo': function() {
            return this['photos[0][file]'];
        }
    }
};

config.store = {
    'service': config.router.base_url,
    'defaults': {'format': 'json'}
};

config.outbox = {};

config.transitions = {
    'default': "slide",
    'save': "flip"
};

for (var key in overrides) {
    config[key] = overrides[key];
}

return config;

});
