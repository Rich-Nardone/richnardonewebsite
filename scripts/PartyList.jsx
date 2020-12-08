import React, { useState, useEffect } from 'react';
import { Socket } from './Socket';
import { fnt, brc } from './OptionMenu';

const div = {
  width: 205,
  height: 200,
  background: 'lightblue',
  border: brc,
};
const p = {
  padding: 0,
  margin: 10,
  position: 'relative',
  border: brc,
  fontWeight: 'bold',
  textAlign: 'center',
  fontSize: fnt,
};
const ul = {
  height: 123,
  textAlign: 'left',
  overflow: 'scroll',
  fontStyle: 'italic',
  padding: 0,
  fontSize: fnt,
};

const listStyle = {
  borderRadius: 5,
  border: brc,
  textAlign: 'center',
  fontWeight: 'bold',
  padding: 2,
  margin: 3,
  fontSize: fnt,
};

export function PartyList() {
  const [party, setParty] = useState([]);

  function retrievePlayerParty() {
    useEffect(() => {
      Socket.emit('get party');
      Socket.on('user party', (data) => {
        setParty(data);
      });
    }, []);
  }
  const displayParty = party.map((members, index) => (
    // eslint-disable-next-line react/no-array-index-key
    <li key={index}>
      {' '}
      {members}
      {' '}
    </li>
  ));

  retrievePlayerParty();
  return (
    <div style={div}>
      <p style={p}> PARTY </p>
      <br />
      <ul style={ul}>
        {' '}
        {displayParty}
        {' '}
      </ul>
    </div>
  );
}

export default PartyList;
