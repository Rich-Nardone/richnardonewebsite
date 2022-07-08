import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { MainUI } from './MainUI';
import { About } from './About';



const uiElement = document.getElementById('main_ui');
if (uiElement) {
  ReactDOM.render(<MainUI />, uiElement);
}

const landingElement = document.getElementById('about_page');
if (landingElement) {
  ReactDOM.render(<About />, landingElement);
}


