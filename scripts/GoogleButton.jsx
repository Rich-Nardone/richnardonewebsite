import * as React from 'react';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';
import { GoogleLogout } from 'react-google-login';
import { ClientID } from './ClientID'

function handleLoginSuccess(response){
    console.log("Successful Login")
    let userData=response
    Socket.emit('google login', {'UserInfo':userData});
    
    
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
            buttonText="Login"
            onSuccess={handleLoginSuccess}
            onFailure={handleLoginFail}
            cookiePolicy={'single_host_origin'}
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
