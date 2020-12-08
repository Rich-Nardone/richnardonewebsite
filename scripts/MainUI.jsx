import React from 'react';
import Sound from 'react-sound';
import { Chatbox } from './Chatbox';
import { InventoryList } from './InventoryList';
import { PartyList } from './PartyList';
import { Socket } from './Socket';
import { volu, fnt, brc } from './OptionMenu';

const button = {
  fontWeight: 'bold',
  fontStyle: 'italic',
  width: 210,
  border: brc,
  fontSize: fnt,
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
      <Sound
        url="static/MainChatTheme.mp3"
        playStatus={Sound.status.PLAYING}
        volume={volu}
      />
      <PartyList />
      <InventoryList />
      <Chatbox />
      <button type="submit" style={button} onClick={gotoOptions}>Options</button>
    </div>
  );
}

export default MainUI;
