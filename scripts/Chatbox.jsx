import React, { useState, useEffect } from 'react';
import { Socket } from './Socket';
import { fnt, brc } from './OptionMenu';

const div = {
  width: 1000,
  height: 430,
  position: 'fixed',
  left: 300,
  top: 50,
  display: 'inline',
  background: 'grey',
  border: brc,
  fontSize: fnt,
  boxShadow: '2px 5px black',
  borderRadius: 10,
};
const ul = {
  listStyleType: 'none',
  height: 315,
  textAlign: 'left',
  overflow: 'scroll',
  fontStyle: 'italic',
  fontWeight: 'bold',
  fontSize: fnt,

};

const input = {

  width: 942,
};
const p = {

  padding: 0,
  margin: 0,
  position: 'relative',
  border: brc,
  fontWeight: 'bold',
  textAlign: 'center',
  opacity: 0.5,
  fontStyle: 'italic',

};

const secretP = {
  textAlign: 'center',
  fontWeight: 'bold',
  fontStyle: 'italic',
  background: 'grey',
  fontSize: fnt,

};

const details = {
  fontWeight: 'bold',
  textAlign: 'center',
  fontStyle: 'italic',
  fontSize: fnt,
};

const body = {
  background: 'grey',
};

export function Chatbox() {

  return (
    <div style={div}>
      <div id="chatbox">
        <ul style={ul}>
        </ul>
      </div>
      <p style={p}>Possible Actions: &quot;Say&quot;, &quot;Do&quot;, &quot;Attack&quot;</p>
      <details>
        <summary style={details}>Pssst..click me for goods</summary>
        <body style={body}>
          <p style={secretP}>
            {' '}
            Welcome to Ghosty&apos;s Emporium! What can I get ye?
          </p>
          <p style={secretP}>
            Current Money:
            {' '}
            Bucks
          </p>
          <br />
        </body>

      </details>
      <br />
      <div id="user_buttons">
       
      </div>
    </div>
  );
}

export default Chatbox;
