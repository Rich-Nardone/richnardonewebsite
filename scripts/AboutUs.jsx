import React from 'react';
import Sound from 'react-sound';

const h1 = {
  textAlign: 'left',
  padding: 50,
  margin: 50,
  width: 300,
  fontWeight: 'bold',
  fontStyle: 'italic',
  borderWidth: 5,
  borderRadius: 10,
  background: 'orange',
  boxShadow: '2px 5px black',

};

const h12 = {
  position: 'relative',
  textAlign: 'left',
  padding: 50,
  margin: 50,
  width: 300,
  left: 300,
  fontWeight: 'bold',
  fontStyle: 'italic',
  borderWidth: 5,
  borderRadius: 10,
  background: 'orange',
  boxShadow: '2px 5px black',

};

const h2O = {

  listStyleType: 'none',
  padding: 0,
  margin: 0,
  textAlign: 'left',
  fontWeight: 'bold',
  fontSize: '25',

};

const h3 = {

  listStyleType: 'none',
  padding: 0,
  margin: 0,
  textAlign: 'left',
  fontWeight: 'bold',
  fontSize: '20',
  background: 'orange',
  borderRadius: 10,
  borderWidth: 5,
  width: 300,
  boxShadow: '2px 5px black',

};

const p = {
  position: 'relative',
  textAlign: 'center',
  fontWeight: 'bold',
  fontStyle: 'italic',
  fontSize: 16,
  background: 'orange',
  borderRadius: 10,
  borderWidth: 5,
  width: 300,
  left: 300,
  boxShadow: '2px 5px black',

};

export function About() {
  function toLogin() {
    window.location = 'login.html';
    return window.location;
  }

  return (
    <div>
      <Sound
        url="static/flute.mp3"
        playStatus={Sound.status.PLAYING}
        volume="50"
      />
      <h1 style={h1}> Welcome to Text RPG </h1>
      <h1 style={h12}> About Us and Acknowledgements! </h1>
      <br />
      <ul style={h2O}>
        <li style={h3}>Who we are</li>

        <p style={p}>
          {' '}
          Just a bunch of CS Majors doing what we love! The people involved are:
          Bartlomiej Rutyna,
          Simon Lam,
          Matthew Carnevale,
          Richard Nardone,and
          Patrick Rosas.
        </p>

        <br />
        <li style={h3}>What we made and what it does </li>

        <p style={p}>
          {' '}
          We made a Text RPG, basically before we had 2D and 3D software in gaming, this is how
          people did RPG&apos;s! With nothing but text, and some imagination. Of course we
          modernised it to make it more appealing to the present day.
        </p>

        <br />
        <li style={h3}>How you made it and what technologies were used</li>

        <p style={p}>
          NANOMACHINES SON. References aside, we used mostly what we used in the previous
          Projects; Python, Flask, React, PSQL, HTML, and our brains!
        </p>
        <br />

        <li style={h3}> Why you&apos;ve made it and why it matters </li>

        <p style={p}>
          {' '}
          Because we want a good grade /s. Also, the journey! You create a whole product with
          a team of people you maybe never met before! The satisfaction of knowing you helped
          make this is also a nice touch.
        </p>
        <br />
      </ul>

      <button type="submit" onClick={toLogin}> Enter Website </button>
    </div>
  );
}

export default About;
