import React, { useState } from 'react';
import { Socket } from './Socket.jsx';


const div_style= {
  textAlign: 'center',
  fontWeight: 'bold',
  fontStyle: 'italic',
  background: 'grey',
  padding: 5,
  margin: 5,
  borderRadius: 10,
  fontSize: 18,
  width: 1500,
  boxShadow:'5px 10px black',
};




export function EmailLogin() {
  const [email, setEmail] = useState(null);

  function checkEmail(event) {
    event.preventDefault();
    event.target.value = '';
    Socket.emit('email login', email);
    Socket.on('email exists', (data) => {
      console.log(data);
      if (data.user_exists && data.has_character) { return window.location = 'character_selection.html'; } // subject to change
      if (data.user_exists && !data.has_character) {
        return window.location = 'character_creation.html';
      }

      alert('Email not found please try again');
      Socket.off('email exists');
    });
  }

  return (
    <div style={div_style}>
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
