import React from 'react'; 
import {GoogleLoginButton} from './GoogleButton.jsx'
import Sound from 'react-sound';
import {EmailLogin} from './EmailLogin.jsx';

const h1={
    textAlign: 'center',
    padding: 50,
    margin: 50,
    fontWeight: 'bold',
    fontStyle: 'italic',
    borderWidth: 5,
    background: 'linear-gradient(darkviolet,darkblue)',
    borderRadius:10
};

const image_style={
    float:'center',
    padding:5,
    margin:5,
    width:1485,
    height:300,
};



export function App(){
    return(
        <div>
            <h1 style={h1}>Welcome to Text RPG</h1>
            <img  style={image_style} src='/static/Fog.gif' alt="image"/>
            <hr></hr>
            <GoogleLoginButton /> 
            <EmailLogin />
            <Sound
                    url='/static/Index_LoginTheme.mp3'
                    playStatus={Sound.status.PLAYING}
                    volume='50'
            />
            <hr></hr>
        </div>
        
        
    );
}