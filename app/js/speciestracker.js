requirejs.config({
    'baseUrl': '/js/lib',
    'paths': {
        'speciestracker': '../speciestracker',
        'data': '../data/'
    }
});

requirejs(['speciestracker/main']);
