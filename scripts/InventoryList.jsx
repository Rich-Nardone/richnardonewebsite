//Displayes inventory list. Inventory list is retrieved from database
import React from 'react'; 


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
    const display_inventory = props.user_content.map((items,index)=>
        <li key={index}> {items} </li>
    );
    
    return(
        <div style={div}>
            <p style={p}> INVENTORY </p>
            <ul style={ul}> {display_inventory} </ul>
        </div> 
    );
}