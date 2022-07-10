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


export function Projects() {

  return (
    <div>
      <NavBar />
    
    </div>
  );
}

export default Projects;
