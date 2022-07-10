import React, { useState, useEffect } from 'react';
import { Socket } from './Socket';
import { fnt, brc } from './OptionMenu';

const div = {
  width: 205,
  height: 200,
  left: 50,
  background: 'lightblue',
  border: brc,
  boxShadow: '2px 5px black',
  borderRadius: 10,
  top: '50%',
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

export function PartyList() {
  const [party, setParty] = useState([]);
  const displayParty = party.map((members, index) => (

    <li key={index}>
      {members}
      {' '}
    </li>
  ));
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
