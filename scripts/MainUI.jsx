import React, {useState, useEffect} from 'react'; 
import { Chatbox } from './Chatbox.jsx';
import { InventoryList } from './InventoryList.jsx'; 
import { PartyList } from './PartyList.jsx';
import {Socket} from './Socket.jsx'; 


export function MainUI(){
    const [player_info, setPlayerInfo] = useState({user_party: [], user_inventory: [], user_chatlog: []});
    
    function retrieve_player_info(){
        useEffect(()=>{
            Socket.emit('user onchat');
            Socket.on('player info', (data)=>{
                setPlayerInfo(data);
            });
        }, []);    
    }
    
    retrieve_player_info()
    
    console.log(player_info);
    return(
        <div>
            <PartyList user_content={player_info.user_party} /> 
            <InventoryList user_content={player_info.user_inventory} />
            <Chatbox user_content={player_info.user_chatlog} /> 
        </div>     
    );
}