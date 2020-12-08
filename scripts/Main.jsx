import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { App } from './App';
import { MainUI } from './MainUI';
import { CreationUI } from './CharCreation';
import { Options } from './OptionMenu';
import { About } from './AboutUs';
import { CharSelection } from './CharSelection';

const loginElement = document.getElementById('login');
if (loginElement) {
  ReactDOM.render(<App />, loginElement);
}

const creationElement = document.getElementById('create_ui');
if (creationElement) {
  ReactDOM.render(<CreationUI />, creationElement);
}

const uiElement = document.getElementById('main_ui');
if (uiElement) {
  ReactDOM.render(<MainUI />, uiElement);
}

const optionElement = document.getElementById('options');
if (optionElement) {
  ReactDOM.render(<Options />, optionElement);
}

const landingElement = document.getElementById('about_page');
if (landingElement) {
  ReactDOM.render(<About />, landingElement);
}

const selectionElement = document.getElementById('selectionUI');
if (selectionElement) {
  ReactDOM.render(<CharSelection />, selectionElement);
}
