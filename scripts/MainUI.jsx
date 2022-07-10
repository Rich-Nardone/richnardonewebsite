import React from 'react';
import { NavBar } from './NavBar';
import { Chatbox } from './Chatbox';
import { PartyList } from './PartyList';
import { volu, fnt, brc } from './OptionMenu';

const button = {
  position: 'relative',
  fontWeight: 'bold',
  fontStyle: 'italic',
  width: 210,
  border: brc,
  fontSize: fnt,
  top: 300,
  borderRadius: 10,
};

export function MainUI() {
  function gotoOptions() {
    // eslint-disable-next-line no-console
    console.log('Heading to Options!');
    window.location = 'options.html';
    return window.location;
  }

  return (
    <div>
      <NavBar />
      <Chatbox />
    </div>
  );
}

export default MainUI;
