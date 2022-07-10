import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { MainUI } from './MainUI';
import { About } from './About';
import { Resume } from './Resume';
import { Projects } from './Projects';
import { Contact } from './Contact';


const uiElement = document.getElementById('main_ui');
if (uiElement) {
  ReactDOM.render(<MainUI />, uiElement);
}

const landingElement = document.getElementById('about_page');
if (landingElement) {
  ReactDOM.render(<About />, landingElement);
}

const resumeElement = document.getElementById('resume_page');
if (resumeElement) {
  ReactDOM.render(<Resume />, resumeElement);
}

const projectsElement = document.getElementById('projects_page');
if (projectsElement) {
  ReactDOM.render(<Projects />, projectsElement);
}

const contactElement = document.getElementById('contact_page');
if (contactElement) {
  ReactDOM.render(<Contact />, contactElement);
}