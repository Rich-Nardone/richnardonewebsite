import * as React from 'react';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';
import { GoogleLogout } from 'react-google-login';

function handleLoginSuccess(response){
    Socket.emit('google login', {'tokenId':response.tokenId});
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
            clientId='656111270790-6jsfgnirr63rvkth2ro0u35l4alkugrg.apps.googleusercontent.com'
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
            clientId="656111270790-6jsfgnirr63rvkth2ro0u35l4alkugrg.apps.googleusercontent.com"
            buttonText="Logout"
            onLogoutSuccess={handleLogoutSuccess}
            onFailure = {handleLogoutFail}
            isSignedIn = {true}
        />    
    );
}
