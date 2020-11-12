import * as React from 'react';
import * as ReactDOM from 'react-dom';

import {App} from './App.jsx'; 
import {MainUI} from './MainUI.jsx'


const loginElement = document.getElementById('login');
if(loginElement){
    ReactDOM.render(<App />, document.getElementById('login'));
}

const uiElement = document.getElementById('main_ui');
if(uiElement){
    ReactDOM.render(<MainUI />, document.getElementById('main_ui'))
}