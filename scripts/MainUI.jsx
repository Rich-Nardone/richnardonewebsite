import React from 'react'; 
import { Chatbox } from './Chatbox.jsx';
import { InventoryList } from './InventoryList.jsx'; 
import { PartyList } from './PartyList.jsx';

export function MainUI(){
    return(
        <div>
            <PartyList /> 
            <InventoryList />
            <Chatbox /> 
        </div>     
    );
}