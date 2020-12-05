import React, {useState, useEffect} from 'react'; 
import { Chatbox } from './Chatbox.jsx';
import { InventoryList } from './InventoryList.jsx'; 
import { PartyList } from './PartyList.jsx';
import {Socket} from './Socket.jsx';
import Sound from 'react-sound';
import {volu} from './OptionMenu.jsx';
import {fnt} from './OptionMenu.jsx';
import {brc} from './OptionMenu.jsx';



const button={
    fontWeight:'bold',
    fontStyle:'italic',
    width:210,
    border:brc,
    fontSize:fnt,
}   



export function MainUI(){
    
    function gotoOptions(){
        
        console.log("Heading to Options!")
        return(window.location = "options.html")
    }
    
    return(
        <div>
            <Sound
                    url='static/MainChatTheme.mp3'
                    playStatus={Sound.status.PLAYING}
                    volume={volu}
            />
            <PartyList /> 
            <InventoryList />
            <Chatbox /> 
            <button style={button} onClick={gotoOptions}>Options</button>
        </div>     
    );
}
