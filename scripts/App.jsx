import React from 'react'; 
import {GoogleLoginButton} from './GoogleButton.jsx'

export function App(){
    return(
        <div>
            <h1>Welcome to Text RPG</h1>
            <h3>For new Users</h3> 
            <GoogleLoginButton /> 
            <h3>For returning Users</h3>
            <p> TODO: add email component </p> 
        </div>
        
    );
}