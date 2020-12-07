import React, {useState, useEffect} from 'react';
import {Socket} from './Socket.jsx'; 

export function CharSelection(){
    const [character, updateCharacter] = useState([]);
    const [selection, updateSelection] = useState(null);
    
    function getCharacters(){
        useEffect(()=>{
            Socket.emit("get user characters");
            Socket.on("recieve user characters", (data)=>{
                updateCharacter(data.char_instance);
                Socket.off("recieve user characters")
            });
            
        }, []);
    }
    
    function newChar(event){
        return window.location="character_creation.html";
    }
    
    const display_character = character.map((chars,index)=>
        <div>
        <input type ="radio" value={chars.id} name="char" onChange={e=>updateSelection(e.target.value)}/>
        <label> Character Name: {chars.character_name} , Class: {chars.class}</label>
        </div>
    );
    
    function toMain(event){
        event.preventDefault();
        Socket.emit("choosen character", selection);
        if(selection != null)
            return window.location = "main_chat.html";
    }
    
    getCharacters();
    return(
        <div>
            <h1> Continue with Charcter </h1> 
            <form onSubmit={toMain}> 
                {display_character}
                <br />
                <input type="submit" /> 
            </form>
            <button onClick={newChar}> Create new Character </button> 
        </div>
    );
}