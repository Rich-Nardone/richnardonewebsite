//Displayes inventory list. Inventory list is retrieved from database
import React, {useState, useEffect} from 'react';
import {Socket} from './Socket.jsx';
import PropTypes from 'prop-types';
import {fnt} from './OptionMenu.jsx';
import {brc} from './OptionMenu.jsx';




const div={
    width:205,
    height: 200,
    background:'orange',
    border:brc,
    
    
    
};
const p={
    padding:'auto',
    margin:10,
    position: 'relative',
    border:brc,
    fontWeight:'bold',
    textAlign:'center',
    fontSize:fnt,
    
};
const ul={
    height: 151,
    textAlign:'left',
    overflow: 'scroll',
    fontStyle:'italic',
    padding:0,
    fontSize:fnt,
   
};

const list_style={
    borderRadius:5,
    border:brc,
    textAlign:'center',
    fontWeight:'bold',
    padding:2,
    margin:3,
    fontSize:fnt,
    
    
}


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
    
    const display_inventory = inventory.map((inventory,index)=>
        <li key={index}> {inventory} </li>
    );
    
    retrieve_player_inventory();
    
    return(
        <div style={div}>
            <p style={p}> INVENTORY </p>
            <ul style={ul}> {display_inventory} </ul>
        </div> 
    );
}