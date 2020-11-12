import React, {useState, useEffect} from 'react';
import {Socket} from './Socket.jsx'; 

export function PartyList(){
    const [currParty, setParty] = useState([]);
    function retrieve_party(){
        useEffect(()=>{
            let isMounted = true;
            Socket.on('user party', (data)=>{
                Socket.emit('user onchat'); //IF this is put outside of the useEffect socket will emit inifinity causing browser to crash .. proceed with caution
                if(isMounted) setParty();
            }); 
            return () =>{isMounted = false;}
        });
        
    }
    
    const display_party = currParty.map((members,index)=>
        <li key={index}> {members} </li>
    );
    
    retrieve_party();
    
    return(
        <div>
            <p> PARTY </p>
            <ul> {display_party} </ul>
        </div> 
    );
}