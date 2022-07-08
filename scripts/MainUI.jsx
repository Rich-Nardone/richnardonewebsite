import React from 'react';
import Sound from 'react-sound';
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
      <Sound
        url="static/MainUIMusic.mp3"
        playStatus={Sound.status.PLAYING}
        volume={volu}
      />
      <PartyList />
      <Chatbox />
      <button type="submit" style={button} onClick={gotoOptions}>Options</button>
    </div>
  );
}

export default MainUI;
