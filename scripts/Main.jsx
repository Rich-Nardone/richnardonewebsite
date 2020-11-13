import * as React from 'react';
import * as ReactDOM from 'react-dom';

import {App} from './App.jsx'; 
import {MainUI} from './MainUI.jsx';
import {CreationUI} from './CharCreation.jsx'


const loginElement = document.getElementById('login');
if(loginElement){
    ReactDOM.render(<App />, document.getElementById('login'));
}

const uiElement = document.getElementById('main_ui');
if(uiElement){
    ReactDOM.render(<MainUI />, document.getElementById('main_ui'))
}

const creationElement = document.getElementById('create_ui'); 
if(creationElement){
    ReactDOM.render(<CreationUI />, document.getElementById('create_ui'));
}