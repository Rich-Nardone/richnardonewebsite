//Displayes inventory list. Inventory list is retrieved from database
import React from 'react';
import PropTypes from 'prop-types';



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
    padding:0,
   
};

const list_style={
    borderRadius:5,
    border:'2px solid black',
    textAlign:'center',
    fontWeight:'bold',
    padding:2,
    margin:3,
    
    
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