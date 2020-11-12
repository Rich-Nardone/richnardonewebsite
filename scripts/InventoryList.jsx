//Displayes inventory list. Inventory list is retrieved from database
import React, {useState, useEffect} from 'react'; 
import {Socket} from './Socket.jsx';

export function InventoryList(){
    const [currInven, setInven] = useState([]);
    
    function retrieve_inventory(){
        useEffect(()=>{
            let isMounted = true;
            Socket.on('user inventory', (data)=>{
                console.log('Socket user invetory emit');
                Socket.emit('user onchat');
                if(isMounted) setInven(data);
            }); 
            return () =>{isMounted = false;}
        });
    }
    
    const display_inventory = currInven.map((items,index)=>
        <li key={index}> {items} </li>
    );
    
    retrieve_inventory();
    
    return(
        <div>
            <p> INVENTORY </p>
            <ul> {display_inventory} </ul>
        </div> 
    );
}