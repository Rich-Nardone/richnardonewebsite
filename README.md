---------------------------------------------------
    PRESENTING!
        THE TEXT RPG ADVENTURE GAME!
            FULL OF FUN AND WONDER!
----------------------------------------------------

Credit to https://www.youtube.com/watch?v=mHBHHEoJ_WA 

### Python install packages 

    pip install Flask
    
    pip install Flask-SQLAlchemy
    
    pip install psycopg2-binary
    
    pip install flask-socketio

    pip install evenlet

    pip install requests

### Npm packages 

    npm install socket.io-client --save  
    npm install --save react-google-button




WARNING: If you receive an error from the command "npm run watch" regarding a missing "babel-loader", run the following:
    npm install --save-dev @babel/core
    npm install --save-dev @babel/preset-react
    npm install babel-loader
------------------------------------------------------------------
!!TO RESOLVE GOOGLEOAUTH LOGIN FAILURE ISSUE!!

1. Touch a file in the repository called ClientID.
2. Make sure you have a client id from the Google API Console, https://developers.google.com/identity/protocols/oauth2 for instructions.
2. Copy and paste this code into it:

    import * as React from 'react';
    import * as ReactDOM from 'react-dom';

    let ClientID = INSERT CLIENT ID HERE

    export {ClientID};

3. Place the file in the "scripts" folder.