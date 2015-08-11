#!/bin/sh

# Exit on error
set -e

if [ -z "$1" -o -z "$2" -o -z "$3" ]; then
   echo "Usage: ./phonegap-build.sh VERSION APPID CREDENTIALS CROSSWALK";
   exit;
fi;

VERSION=$1
API=https://build.phonegap.com/api/v1/
APPID=$2
CREDENTIALS=$3
CROSSWALK=$4
CONFIG=`curl -s http://species.wq.io/config.json`
CONTEXT="--context {\"version\":\"$VERSION\",\"crosswalk\":\"$CROSSWALK\"}"

# Build javascript with wq.app
cd ../app
echo "define($CONFIG);" > js/data/config.js
wq build $VERSION

# Copy important stuff from wq build
cd ../native
rm -rf build
mkdir build
mkdir build/js
mkdir build/js/lib
mkdir build/css
mkdir build/css/lib
cp -p ../htdocs-build/js/species.js build/js/
cp -p ../htdocs-build/js/lib/require.js build/js/lib/
cp -p ../htdocs-build/css/species.css build/css/
cp -a ../htdocs-build/css/lib/images build/css/lib/
cp -a ../htdocs-build/images build/

# Compile index & config templates
wq mustache --template index.html --output build/index.html $CONTEXT
wq mustache --template config.xml --output build/config.xml $CONTEXT

# Upload zip file to phonegap build
cd build
zip -r species-$VERSION.zip *
curl -F file=@species-$VERSION.zip -u $CREDENTIALS -X PUT $API/apps/$APPID
