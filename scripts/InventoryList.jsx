//Displayes inventory list. Inventory list is retrieved from database
import React from 'react'; 

export function InventoryList(props){
    const display_inventory = props.user_content.map((items,index)=>
        <li key={index}> {items} </li>
    );
    
    return(
        <div>
            <p> INVENTORY </p>
            <ul> {display_inventory} </ul>
        </div> 
    );
}