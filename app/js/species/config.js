define(["data/config", "data/version"],
function(config, version) {

config.defaults = {
    'version': version
};

config.transitions = {
    'default': "slide",
    'save': "flip"
};

config.map = {
    'zoom': 12,
    'center': [45.3, -107.5]
};

return config;

});
