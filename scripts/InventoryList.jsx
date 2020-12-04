//Displayes inventory list. Inventory list is retrieved from database
import React from 'react';
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
    const display_inventory = props.user_content.map((items,index)=>
        <li style={list_style} key={index}> {items} </li>
    );
    
    return(
        <div style={div}>
            <p style={p}> INVENTORY </p>
            <ul style={ul}> {display_inventory} <br></br></ul>
        </div> 
    );
}

InventoryList.propTypes = {
    user_content: PropTypes.array,
};