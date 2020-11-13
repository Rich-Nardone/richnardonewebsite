  
import React from 'react';


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

export function PartyList(props){
    console.log(props);
    const display_party = props.user_content.map((members,index)=>
        <li key={index}> {members} </li>
    );
    
    return(
        <div style={div}>
            <p style={p}> PARTY </p>
            <br></br>
            <ul style={ul}> {display_party} </ul>
        </div> 
    );
}