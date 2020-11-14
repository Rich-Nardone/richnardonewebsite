#!usr/bin/env bash

# In case pip doesn't work
PIP=$(which pip)
# Change this to "ddd" if you want to look like a hackerman
MODE=s

# Python and relevant directories
echo "Checking Python..."
python --version || npm install -g python
echo "...for requests"
sudo ${PIP} install requests -q
# flask serving
echo "...for Flask"
sudo ${PIP} install flask -q
echo "...for flask-socketio"
sudo ${PIP} install flask-socketio -q
echo "...for eventlet"
sudo ${PIP} install eventlet -q
# psql dependencies
echo "...for psycopg2-binary"
sudo ${PIP} install psycopg2-binary -q
echo "...for Flask-SQLAlchemy"
sudo ${PIP} install Flask-SQLAlchemy==2.1 -q
# code coverage and testing
echo "...for coverage"
sudo ${PIP} install coverage -q
echo "...for pylint"
sudo ${PIP} install pylint
echo "...for black"
sudo ${PIP} install git+git://github.com/psf/black

echo "Updating npm and dependencies..."
npm install -${MODE}
npm install -g webpack -${MODE}
npm install --save-dev webpack -${MODE}
npm install socket.io-client --save -${MODE}
# google auth
npm install --save react-google-button -${MODE}
# for linting
npm install eslint --save-dev -${MODE}
npm install eslint-plugin-react@latest --save-dev -${MODE}
npm i eslint-config-airbnb -${MODE}
npm install eslint-plugin-jsx-a11y@latest --save-dev -${MODE}
npm install eslint-plugin-import@latest --save-dev -${MODE}

echo "All dependencies installed!"