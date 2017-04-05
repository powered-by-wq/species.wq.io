function getBaseUrl() {
    var baseurl = window.location.pathname.replace("index.html",'');
    baseurl = baseurl.replace(/\/$/,'');
    if (baseurl == 'www') {
        // Windows
        baseurl = '/www';
    }
    return baseurl;
}

require.config({
    'config': {
        'speciestracker/config': {
             'router': {
                 'base_url': getBaseUrl()
             },
             'store': {
                 'service': 'https://species.wq.io',
                 'defaults': {'format': 'json'}
             },
        }
    }
});

document.addEventListener('deviceready', function() {
    require(['js/speciestracker'], function() {
        require(['speciestracker/main', 'wq/app'], function(ready, app) {
            ready.then(function() {
                app.replaceState('');
                setTimeout(navigator.splashscreen.hide, 10);
            });
        });
    });
});
