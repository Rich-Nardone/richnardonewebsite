  
import React from 'react';

export function PartyList(props){
    console.log(props);
    const display_party = props.user_content.map((members,index)=>
        <li key={index}> {members} </li>
    );
    
    return(
        <div>
            <p> PARTY </p>
            <ul> {display_party} </ul>
        </div> 
    );
}