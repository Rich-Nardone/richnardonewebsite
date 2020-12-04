import React from 'react';
import PropTypes from 'prop-types';
import {fnt} from './OptionMenu.jsx';
import {brc} from './OptionMenu.jsx';

const div={
    width:205,
    height: 200,
    background:'lightblue',
    border:brc,
    
    
};
const p={
    padding:0,
    margin:10,
    position: 'relative',
    border:brc,
    fontWeight:'bold',
    textAlign:'center',
    fontSize:fnt,
   
    
    
    
    
};
const ul={
    height: 123,
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

export function PartyList(props){
    console.log(props);
    const display_party = props.user_content.map((members,index)=>
        <li style={list_style} key={index}> {members} </li>
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

