import React from 'react';
import Sound from 'react-sound';

const h1 = {
  textAlign: 'center',
  marginTop:200,
  width:'100%',
  fontWeight: 'bold',
  fontStyle: 'italic',
  borderWidth: 5,
  borderRadius: 10,
  background: 'orange',
  boxShadow: '2px 5px black',

};

const div1 = {

  display: 'block',
  marginLeft: 'auto',
  marginRight: 'auto',
  width: '40%',
  fontWeight: 'bold',
  fontStyle: 'italic',
  alignItems:'center'
};

const p = {
  textAlign: 'center',
  fontWeight: 'bold',
  fontStyle: 'italic',
  fontSize: 16,
  background: 'orange',
  borderRadius: 10,
  borderWidth: 5,
  width: 300,
  boxShadow: '2px 5px black',
  display: 'block',
  marginLeft: 'auto',
  marginRight: 'auto',
};

export function About() {
  function toEnter() {
    window.location = 'main_chat.html';
    return window.location;
  }

  return (
    <div style={div1}>
      <h1 style={h1}> Richard Nardone Portfolio Website </h1>

      <br />

      <p style={p}>
        Built Using Python, Flask, React, PSQL, HTML
      </p>
      <br />
      <br />

      <button style= {p} type="submit" onClick={toEnter}> Enter Website </button>
    </div>
  );
}

export default About;
