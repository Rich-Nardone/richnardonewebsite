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
echo "...for flask-session"
sudo ${PIP} install Flask-Sessions -q
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
sudo ${PIP} install pylint -q
echo "...for black"
sudo ${PIP} install git+git://github.com/psf/black -q

echo "Updating npm and dependencies..."
npm i -s
npm i -g webpack -${MODE}
npm i --save-dev webpack -${MODE}
npm i -S webpack-cli -${MODE}
npm i -S socket.io-client -${MODE}
# react
npm i -S react -${MODE}
npm i -S react-dom -${MODE}
npm i -S react-sound -${MODE}
# google auth
npm i -S react-google-button -${MODE}
npm i -S react-google-login -${MODE}
# for linting
npm i eslint --save-dev -${MODE}
npm i eslint-plugin-react@latest --save-dev -${MODE}
npm i eslint-config-airbnb -${MODE}
npm i eslint-plugin-jsx-a11y@latest --save-dev -${MODE}
npm i eslint-plugin-import@latest --save-dev -${MODE}
# other
npm i -S prop-types -${MODE}

echo "All dependencies installed!"