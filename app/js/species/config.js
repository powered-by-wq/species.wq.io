define(["data/config", "data/templates", "data/version", "module"],
function(config, templates, version, module) {

var overrides = module.config();

config.template = {
    'templates': templates,
    'defaults': {
        'version': version,
        'first_photo': function() {
            if (this.photos && this.photos.length) {
                return this.photos[0];
            } else {
                return this.photos;
            }
        }
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
