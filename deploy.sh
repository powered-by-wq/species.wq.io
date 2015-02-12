#!/bin/sh

# Exit on error
set -e

# Dump wq configuration object to file (requires Django 1.7)
CONFIG=`db/manage.py dump_config`
echo "define($CONFIG);" > app/js/data/config.js

# Build javascript with wq.app
cd app;
wq build $1;

# Force important files through any unwanted server caching
cd ../;
sed -i "s/species.js/species.js?v="$1"/" htdocs-build/species.appcache
sed -i "s/species.css/species.css?v="$1"/" htdocs-build/species.appcache

# Preserve Django's static files (e.g. admin)
if [ -d htdocs/static ]; then
    cp -a htdocs/static htdocs-build/static
fi;

# Replace existing htdocs with new version
rm -rf htdocs/;
mv -i htdocs-build/ htdocs;

# Restart Django
touch db/species/wsgi.py
