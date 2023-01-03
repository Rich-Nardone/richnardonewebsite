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
    marginLeft: 'auto',
    marginRight: 'auto',
    verticalAlign: 'middle',
    width: '500px',
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

const h = {
        textAlign:'center',
        fontStyle:'bold',
        fontSize:32,
        marginLeft: 'auto',
        marginRight: 'auto',
        verticalAlign: 'middle',
        width: '800px',
        display: 'block',
}
export function Resume() {

  return (
    <div>
      <NavBar />
      <br />
      <h2 style = {h}>Resume</h2>
      <embed src="/static/Richard_Nardone_Resume.pdf" width="100%" height="2100px" />
      
    </div>
  );
}

export default Resume;
