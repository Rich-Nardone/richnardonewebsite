/* eslint-disable no-console */
/* eslint-disable no-alert */
import React, { useEffect } from 'react';
import { GoogleLogin, GoogleLogout } from 'react-google-login';
import { Socket } from './Socket';

import { ClientID } from './ClientID';

const logStyle = {
  textAlign: 'center',
  fontWeight: 'bold',
  fontStyle: 'italic',
  background: 'linear-gradient(darkviolet,darkblue)',
  padding: 5,
  margin: 5,
  borderRadius: 10,
  fontSize: 18,
  width: 1500,

};

function handleLoginFail() {
  alert('Google Login in Error');
}
function handleLogoutSuccess() {
  console.log('user logged out');
}
function handleLogoutFail() {
  alert('Google logout failed');
}
export function GoogleLoginButton() {
  function handleLoginSuccess(response) {
    const userData = response;
    Socket.emit('google login', { UserInfo: userData });
  }

  function userHasChar() {
    useEffect(() => {
      Socket.on('google login response', (data) => {
        console.log(data);
        if (data.has_character) { return window.location = 'character_selection.html'; }
        return window.location = 'character_creation.html';
      });
    });
  }

  userHasChar();

  return (
    <GoogleLogin
      clientId={ClientID}
      render={(renderProps) => (
        <button onClick={renderProps.onClick} style={logStyle}>Newcomer? Enter if you dare...</button>
      )}
      buttonText="REGISTER"
      onSuccess={handleLoginSuccess}
      onFailure={handleLoginFail}
      cookiePolicy="single_host_origin"
      theme="dark"
      style={logStyle}

    />
  );
}

export function GoogleLogoutButton() {
  return (
    <GoogleLogout
      clientId={ClientID}
      buttonText="Logout"
      onLogoutSuccess={handleLogoutSuccess}
      onFailure={handleLogoutFail}
      isSignedIn
    />
  );
}
