/* eslint-disable no-alert */
/* eslint-disable no-console */
import React, { useState } from 'react';
import { Socket } from './Socket';

const divStyle = {
  textAlign: 'center',
  fontWeight: 'bold',
  fontStyle: 'italic',
  background: 'grey',
  padding: 5,
  margin: 5,
  borderRadius: 10,
  fontSize: 18,
  width: 1500,
  boxShadow: '5px 10px black',
};

export function EmailLogin() {
  const [email, setEmail] = useState(null);

  function checkEmail(event) {
    event.preventDefault();
    // eslint-disable-next-line no-param-reassign
    event.target.value = '';
    Socket.emit('email login', email);
    Socket.on('email exists', (data) => {
      console.log(data);
      if (data.user_exists && data.has_character) {
        window.location = 'character_selection.html';
        return window.location;
      } // subject to change
      if (data.user_exists && !data.has_character) {
        window.location = 'character_creation.html';
        return window.location;
      }

      alert('Email not found please try again');
      Socket.off('email exists');
      return window.location;
    });
  }

  return (
    <div style={divStyle}>
      <h3> Email Login </h3>
      <form onSubmit={checkEmail}>
        <p> Enter your email </p>
        <input type="text" onChange={(e) => setEmail(e.target.value)} />
        {' '}
        <br />
        <input type="submit" />
      </form>
    </div>
  );
}

export default EmailLogin;
