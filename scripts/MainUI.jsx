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
const h = {
  textAlign:'center',
  fontStyle:'bold',
  fontSize:50,
  marginLeft: 'auto',
  marginRight: 'auto',
  verticalAlign: 'middle',
  width: '800px',
  display: 'block',
}

const div ={
  textAlign: 'center',
  fontStyle:'italic',
  fontSize:32,
  marginLeft: 'auto',
  marginRight: 'auto',
  verticalAlign: 'middle',
  width: '800px',
  display: 'block',
}
export function MainUI() {

  return (
    <div>
      <NavBar />
    <div style = {div}>
      
      <br />
      <br />
        <h2 style = {h}>Home Page</h2>
        <br />
        <p>This website was designed and built by Richard Nardone.</p>
        <p>Resume section includes an embedded form of my Resume for viewing and downloading.</p>
        <p>Projects section includes a brief description of 5 projects I have worked on in the past year along with a link to view the code on my Github.</p>
        <p>Contact Section includes my contact information and links to my socials. </p>
        <p>Thank you for visiting!</p>
        <br />
    </div>
    </div>
  );
}

export default MainUI;
