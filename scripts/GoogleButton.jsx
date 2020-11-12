import * as React from 'react';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';
import { GoogleLogout } from 'react-google-login';
import { ClientID } from './ClientID'

const log_style={
    textAlign:'center',
    fontWeight:'bold',
    fontStyle:'italic',
    background: 'linear-gradient(darkviolet,darkblue)',
    padding: 5,
    margin: 5,
    borderRadius:10,
    fontSize:18,
    width:1500,
    
};


function handleLoginSuccess(response){
    console.log("Successful Login")
    let userData=response
    Socket.emit('google login', {'UserInfo':userData});
    return(
        window.location = "main_chat.html")
}

function handleLoginFail(){
    alert('Google Login in Error');
}
function handleLogoutSuccess(){
    console.log('user logged out');
}
function handleLogoutFail(){
    alert('Google logot failed');
}
export function GoogleLoginButton(){
    return(
        <GoogleLogin 
            clientId={ClientID}
            render={renderProps => (
            <button onClick={renderProps.onClick} style={log_style}>Newcomer? Enter if you dare...</button>
            )}
            buttonText="REGISTER"
            onSuccess={handleLoginSuccess}
            onFailure={handleLoginFail}
            cookiePolicy={'single_host_origin'}
            theme='dark'
            style={log_style}
            
            
            
        />
    );
}

export function GoogleLogoutButton(){
    return(
        <GoogleLogout
            clientId={ClientID}
            buttonText="Logout"
            onLogoutSuccess={handleLogoutSuccess}
            onFailure = {handleLogoutFail}
            isSignedIn = {true}
        />    
    );
}
