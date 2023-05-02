#/bin/sh

python -m venv .
source ./bin/activate
./bin/pip install setuptools==67.7.1 zc.buildout==3.0.1
./bin/buildout -c $1
