/* eslint-disable jsx-a11y/label-has-associated-control */
import React, { useState, useEffect } from 'react';
// eslint-disable-next-line no-unused-vars
import { Socket } from './Socket';
import Sound from 'react-sound';

const h1 = {
  textAlign: 'left',
  padding: 5,
  margin: 5,
  fontWeight: 'bold',
  fontStyle: 'italic',
  borderWidth: 5,
  background: 'grey',
  borderRadius: 10,
  boxShadow:'2px 5px black',
  backgroundPosition: 'center',
  width:500,
};

const character_style ={
  
  textAlign: 'left',
  fontWeight:'bold',
  background: 'grey',
  borderRadius: 5,
  padding: 5,
  margin: 5,
  width:300,
  boxShadow:'2px 5px black',
  
  
  
}


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

  function newChar(event) {
    return window.location = 'character_creation.html';
  }

  const displayCharacter = character.map((chars, index) => (
    <div>
      <input type="radio" value={chars.id} name="char" onChange={(e) => updateSelection(e.target.value)} />
      <label style={character_style} >
        {' '}
        Character Name:
        {chars.character_name}
        {' '}
        , Class:
        {chars.class}
      </label>
      <br></br>
      <br></br>
    </div>
    
  ));

  function toMain(event) {
    event.preventDefault();
    Socket.emit('choosen character', selection);
    if (selection != null) { return window.location = 'main_chat.html'; }
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
      <br></br>
      <form onSubmit={toMain}>
        {displayCharacter}
        <br />
        <input type="submit" />
      </form>
      <button onClick={newChar}> Create new Character </button>
    </div>
  );
}

export default CharSelection;
