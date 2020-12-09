/* eslint-disable jsx-a11y/label-has-associated-control */
import React, { useState, useEffect } from 'react';
import Sound from 'react-sound';
import { Socket } from './Socket';

const h1 = {
  textAlign: 'left',
  padding: 5,
  margin: 5,
  fontWeight: 'bold',
  fontStyle: 'italic',
  borderWidth: 5,
  background: 'grey',
  borderRadius: 10,
  boxShadow: '2px 5px black',
  backgroundPosition: 'center',
  width: 500,
};

const characterStyle = {

  textAlign: 'left',
  fontWeight: 'bold',
  background: 'grey',
  borderRadius: 5,
  padding: 5,
  margin: 5,
  width: 300,
  boxShadow: '2px 5px black',

};

export function CharSelection() {
  const [character, updateCharacter] = useState([]);
  const [selection, updateSelection] = useState(null);

  function getCharacters() {
    useEffect(() => {
      Socket.emit('get user characters');
      Socket.on('recieve user characters', (data) => {
        updateCharacter(data.char_instance);
        Socket.off('recieve user characters');
      });
    }, []);
  }

  function newChar() {
    window.location = 'character_creation.html';
    return window.location;
  }

  const displayCharacter = character.map((chars) => (
    <div>
      <input type="radio" value={chars.id} name="char" onChange={(e) => updateSelection(e.target.value)} />
      <label style={characterStyle}>
        {' '}
        Character Name:
        {chars.character_name}
        {' '}
        , Class:
        {chars.class}
      </label>
      <br />
      <br />
    </div>

  ));

  function toMain(event) {
    event.preventDefault();
    Socket.emit('choosen character', selection);
    if (selection != null) {
      window.location = 'main_chat.html';
    }
    return window.location;
  }

  getCharacters();
  return (
    <div>
      <Sound
        url="/static/Login.mp3"
        playStatus={Sound.status.PLAYING}
        volume="50"
      />
      <h1 style={h1}> Continue with Character? </h1>
      <br />
      <form onSubmit={toMain}>
        {displayCharacter}
        <br />
        <input type="submit" />
      </form>
      <button type="submit" onClick={newChar}> Create new Character </button>
    </div>
  );
}

export default CharSelection;
