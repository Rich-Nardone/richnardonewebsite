import React from 'react';

export function About() {
  function toLogin(event) {
    window.location = 'login.html';
    return window.location;
  }

  return (
    <div>
      <h1> Welcome to Text RPG </h1>
      <p> About Us </p>
      <ul>
        <li>Who we are</li>
        <p> [Enter info here] </p>
        <li>What we made and what it does </li>
        <p> [Enter info here] </p>
        <li>How you made it and what technologies were used</li>
        <p> [Enter info here] </p>
        <li> Why you&apos;ve made it and why it matters </li>
        <p> [Enter info here] </p>
      </ul>

      <button type="submit" onClick={toLogin}> Enter Website </button>
    </div>
  );
}

export default About;
