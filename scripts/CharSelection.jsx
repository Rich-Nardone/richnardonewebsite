import React, {useState, useEffect} from 'react';
import {Socket} from './Socket.jsx'; 

export function CharSelection(){
    const [character, updateCharacter] = useState("empty");
    
    function getCharacters(){
        //use socket
    }
    
    function newChar(event){
        return window.location="character_creation.html";
    }
    
    function toMain(event){
        event.preventDefault(); 
        console.log(character);
        return window.location = "main_chat.html";
    }
    
    return(
        <div>
            <h1> Continue with Charcter </h1> 
            <form onSubmit={toMain}> 
                <input type="radio" 
                id="select1" 
                name="gender" 
                value="char1"
                onChange = {e=>updateCharacter(e.target.value)}
                />
                <label for="select1">Selection Character 1</label><br />
                <input type="radio" 
                id="select2" 
                name="gender" 
                value="char2" 
                onChange = {e=>updateCharacter(e.target.value)}
                />
                <label for="select2">Select Character 2</label><br />
                <input type="radio" 
                id="select3" 
                name="gender" 
                value="char3" 
                onChange = {e=>updateCharacter(e.target.value)}
                />
                <label for="select3">Select Character 3</label>
                <input type="submit" /> 
            </form>
            <button onClick={newChar}> Create new Character </button> 
        </div>
    );
}