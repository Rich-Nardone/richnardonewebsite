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


export function Resume() {

  return (
    <div>
      <NavBar />
      <embed src="/static/RichardNardoneResume.pdf" width="100%" height="2100px" />
      
    </div>
  );
}

export default Resume;
