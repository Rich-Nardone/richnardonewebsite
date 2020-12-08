/* eslint-disable jsx-a11y/label-has-associated-control */
import React, { useState } from 'react';
// eslint-disable-next-line no-unused-vars
import { Socket } from './Socket';

export default function CharSelection() {
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
      <label>
        {' '}
        Character Name:
        {chars.character_name}
        {' '}
        , Class:
        {chars.class}
      </label>
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
      <h1> Continue with Charcter </h1>
      <form onSubmit={toMain}>
        {displayCharacter}
        <br />
        <input type="submit" />
      </form>
      <button onClick={newChar}> Create new Character </button>
    </div>
  );
}
