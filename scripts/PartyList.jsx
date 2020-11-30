import React, {useState, useEffect} from 'react'; 
import {Socket} from './Socket.jsx';

const div={
    width:200,
    height: 200,
    background:'lightblue',
    border:'3px solid black',
    
    
};
const p={
    padding:0,
    margin:10,
    position: 'relative',
    border:'2px solid black',
    fontWeight:'bold',
    textAlign:'center',
   
    
    
    
    
};
const ul={
    height: 123,
    textAlign:'left',
    overflow: 'scroll',
    fontStyle:'italic',
   
};

export function PartyList(){
    
    const[party, setParty] = useState([]);
    
    function retrieve_player_party(){
        useEffect(()=>{
            Socket.emit('get party');
            Socket.on('user party', (data)=>{
                setParty(data);
            });
        }, []);    
    }
    const display_party = party.map((members,index)=>
        <li key={index}> {members} </li>
    );
    
    retrieve_player_party();
    return(
        <div style={div}>
            <p style={p}> PARTY </p>
            <br></br>
            <ul style={ul}> {display_party} </ul>
        </div> 
    );
}

