---------------------------------------------------------------------------
    PRESENTING!
        THE TEXT RPG ADVENTURE GAME!
            FULL OF FUN AND WONDER!
---------------------------------------------------------------------------

Heroku Link:

CREDITS:
==============================================================================================================================================================
Credit to https://www.youtube.com/watch?v=mHBHHEoJ_WA 
Credit to https://www.youtube.com/watch?v=KZZKzJTGI9E&list=PLC0C2A6BCA6040BC8&index=13 and https://www.youtube.com/watch?v=BYP6wlg3MdA for conversion to mp3, 
    Credit to Interplay and Mark Morgan for the soundtrack found in Fallout 1.
==============================================================================================================================================================
To run and install all packages: Run this script: sh tools/install_script.sh
==============================================================================================================================================================
If issues arise and one is unable to run the above script, run these commands in your environment, preferably AWS C9.

---------------------------------------------------------PYTHON LIBRARIES----------------------------------------------------------------------------------------

    pip install Flask
    
    pip install Flask-SQLAlchemy
    
    pip install psycopg2-binary
    
    pip install flask-socketio

    pip install evenlet

    pip install requests
    
    Note: Install python-dotenv via sudo pip install sudo pip install python-dotenv 
--------------------------------------------------------NPM LIBRARIES---------------------------------------------------------------------------------------------


    npm install socket.io-client --save  
    npm install --save react-google-button

WARNING: If you receive an error from the command "npm run watch" regarding a missing "babel-loader", run the following:
    npm install --save-dev @babel/core
    npm install --save-dev @babel/preset-react
    npm install babel-loader
------------------------------------------------------------------------------------------------------------------------------------------------------------------
!!TO RESOLVE GOOGLEOAUTH LOGIN FAILURE ISSUE!!

1. Touch a file in the repository called ClientID.
2. Make sure you have a client id from the Google API Console, https://developers.google.com/identity/protocols/oauth2 for instructions.
2. Copy and paste this code into it:

    import * as React from 'react';
    import * as ReactDOM from 'react-dom';

    let ClientID = INSERT CLIENT ID HERE

    export {ClientID};

3. Place the file in the "scripts" folder.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
WORK DONE BY EACH MEMBER OF THE TEAM
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Simon Lam:
    -Base game logic, game story, scripts in tools folder.

Matthew Carnevale
    -Database setup and connectivity.

Patrick Rosas
    -Created frontend UI's

Richard Nardone
    -Character creation backend

Bartlomiej Rutyna
    -Styling for UI's, HTML Page Re-direct, and Shop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------