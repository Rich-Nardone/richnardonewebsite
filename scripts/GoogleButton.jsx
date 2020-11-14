import * as React from 'react';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';
import { GoogleLogout } from 'react-google-login';
import { ClientID } from './ClientID.jsx';


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




<<<<<<< HEAD

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




=======
>>>>>>> 28ccc9f687de837e19f46273f5c4002c8a654afe
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
    function handleLoginSuccess(response){
        console.log("Successful Login")
        let userData=response
        Socket.emit('google login', {'UserInfo':userData});
<<<<<<< HEAD
        return(window.location = "main_chat.html")
    }
    return(
        <GoogleLogin 
            clientId='517598503885-sqqh5dnpi8hc9dtndgl6uitqvdar1h80.apps.googleusercontent.com'
=======
        return(window.location = "character_creation.html")
    }
    return(
        <GoogleLogin 
            clientId={ClientID}
>>>>>>> 28ccc9f687de837e19f46273f5c4002c8a654afe
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
<<<<<<< HEAD
            clientId='517598503885-sqqh5dnpi8hc9dtndgl6uitqvdar1h80.apps.googleusercontent.com'
=======
            clientId={ClientID}
>>>>>>> 28ccc9f687de837e19f46273f5c4002c8a654afe
            buttonText="Logout"
            onLogoutSuccess={handleLogoutSuccess}
            onFailure = {handleLogoutFail}
            isSignedIn = {true}
        />    
    );
}