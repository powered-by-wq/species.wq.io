requirejs.config({
    'baseUrl': '/js/lib',
    'paths': {
        'species': '../species',
        'data': '../data/'
    }
});

requirejs(['species/main']);
