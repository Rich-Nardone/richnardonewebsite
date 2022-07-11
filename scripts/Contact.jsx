import React from 'react';
import { NavBar } from './NavBar';
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

const div ={
    textAlign: 'center',
    fontStyle:'bold',
    fontSize:32,
    marginLeft: 'auto',
    marginRight: 'auto',
    verticalAlign: 'middle',
    width: '800px',
    display: 'block',
}
const resumeOutline = {
    position: 'relative',
    fontWeight: 'bold',
    fontStyle: 'italic',
    backgroundColor: 'white',
    fontColor: 'black',
    float: 'left',
    clear: 'left',
  };

  const color = {
    fontColor:'red'
  }

export function Contact() {

  return (
    <div>
      <NavBar />
      <div style={div}>
        <br />
        <h2>Contact Information</h2>
        <p>Email: richardmnardone@gmail.com</p>
        <p>Phone Number: (908) 358 - 6664</p>
        <p>   LinkedIn: <a style={color}href='https://www.linkedin.com/in/richardmnardone/'>https://www.linkedin.com/in/richardmnardone/</a></p>
        <p>   Github: <a style={color}href='https://github.com/Rich-Nardone'>https://github.com/Rich-Nardone</a></p>
      </div>
    </div>
  );
}

export default Contact;
