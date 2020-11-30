//Displayes inventory list. Inventory list is retrieved from database
import React, {useState, useEffect} from 'react'; 
import {Socket} from './Socket.jsx'; 



const div={
    width:200,
    height: 200,
    background:'orange',
    border:'3px solid black',
    
    
};
const p={
    padding:'auto',
    margin:10,
    position: 'relative',
    border:'2px solid black',
    fontWeight:'bold',
    textAlign:'center',
    
};
const ul={
    height: 151,
    textAlign:'left',
    overflow: 'scroll',
    fontStyle:'italic',
   
};

export function InventoryList(props){
    const[inventory, setInventory] = useState([]);
    
    function retrieve_player_inventory(){
        useEffect(()=>{
            Socket.emit('get inventory');
            Socket.on('user inventory', (data)=>{
                setInventory(data);
            });
        }, []);    
    }
    
    const display_inventory = inventory.map((items,index)=>
        <li key={index}> {items} </li>
    );
    
    retrieve_player_inventory();
    
    return(
        <div style={div}>
            <p style={p}> INVENTORY </p>
            <ul style={ul}> {display_inventory} </ul>
        </div> 
    );
}
