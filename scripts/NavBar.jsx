import React from 'react';




export function NavBar() {
    const goToPage = e => {
        e.preventDefault();
        // eslint-disable-next-line no-console
        console.log(e.currentTarget.id);
        window.location = e.currentTarget.id+'.html'
        return window.location;
      }
    return (
        <ul>
            <li><button id='main_chat' onClick={goToPage} >Home</button></li>
            <li><button id='resume' onClick={goToPage} >Resume</button></li>
            <li><button id='projects' onClick={goToPage} >Projects</button></li>
            <li><button id='contact' onClick={goToPage} >Contact</button></li>
        </ul>
    );
  }
  
  export default NavBar;
  