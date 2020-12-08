/* eslint-disable jsx-a11y/label-has-associated-control */
/* eslint-disable no-console */
import React, { useState } from 'react';
import Sound from 'react-sound';
import { Socket } from './Socket';

const h1 = {
  textAlign: 'center',
  padding: 50,
  margin: 50,
  fontWeight: 'bold',
  fontStyle: 'italic',
  borderWidth: 5,
  background: 'white',
  borderRadius: 10,
};

const label1 = {
  fontWeight: 'bold',
  fontStyle: 'italic',
  textAlign: 'center',
};

const label2 = {
  fontWeight: 'bold',
  fontStyle: 'italic',
  textAlign: 'center',
  fontSize: '25',
};

const form = {
  background: 'white',
  border: '3px solid black',
  textAlign: 'center',
  borderRadius: 10,
};

function CharSelection() {
  const [charName, setName] = useState('');
  const [gender, setGender] = useState('');
  const [charClass, setCharClass] = useState('');

  function handleForm(event) {
    event.preventDefault();
    const character = {
      name: charName,
      gen: gender,
      classType: charClass,
    };
    console.log('sent to server!');
    console.log(character);
    Socket.emit('user new character', character);
    window.location = 'main_chat.html';
    return window.location;
  }

  return (
    <div>
      <h1 style={h1}>Who Are You?</h1>
      <Sound
        url="static/CharCreation.mp3"
        playStatus={Sound.status.PLAYING}
        volume="50"
      />
      <form style={form} onSubmit={handleForm}>
        <br />
        <label style={label2}> What is your name: </label>
        <br />
        <input type="text" onChange={(e) => setName(e.target.value)} />
        <p style={label2}>What is your gender?</p>
        <label style={label1}> Male </label>
        <input type="radio" name="gender" value="male" onChange={(e) => setGender(e.target.value)} />
        <label style={label1}> Female </label>
        <input type="radio" name="gender" value="female" onChange={(e) => setGender(e.target.value)} />
        <br />
        <br />
        <p style={label2}>What is your class?</p>
        <label style={label1}> Jock </label>
        <input type="radio" name="charclass" value="Jock" onChange={(e) => setCharClass(e.target.value)} />
        <br />
        <label style={label1}> Bookworm </label>
        <input type="radio" name="charclass" value="Bookworm" onChange={(e) => setCharClass(e.target.value)} />
        <br />
        <label style={label1}> NEET </label>
        <input type="radio" name="charclass" value="NEET" onChange={(e) => setCharClass(e.target.value)} />
        <br />
        <br />

        <input type="submit" />
      </form>
    </div>
  );
}
export function CreationUI() {
  return (
    <CharSelection />
  );
}

export default CreationUI;
