import React, {useState} from 'react'; 
import {Socket} from './Socket.jsx';

function CharSelection(){
    const[charName, setName] = useState(''); 
    const[gender, setGender] = useState(''); 
    const[charClass, setCharClass] = useState('');
    
    function handleForm(event){
        event.preventDefault();
        let character = {
            name: charName, 
            gen : gender, 
            classType : charClass
        }
        console.log('sent to server!');
        console.log(character);
        Socket.emit('user new character', character);
        
    }
    
    return(
        <div>
            <form onSubmit={handleForm}> 
                <label> Enter Name: </label> 
                <input type='text' onChange={e =>setName(e.target.value)}/> 
                <br />
                
                <label> Male </label> 
                <input type='radio' name = 'gender' value='male'  onChange={e => setGender(e.target.value)}/>
                <label> Female </label>
                <input type='radio' name = 'gender' value='female' onChange={e => setGender(e.target.value)}/>
                <br />
                
                <label> Sourcer </label>
                <input type='radio' name ='charclass' value='Sourcer' onChange={e => setCharClass(e.target.value)} />
                <label> Barbarian </label>
                <input type='radio' name ='charclass' value='Barbarian' onChange={e => setCharClass(e.target.value)} />
                <label> Rogue </label>
                <input type='radio' name ='charclass' value='Rogue' onChange={e => setCharClass(e.target.value)} />
                <br /> 
                
                <input type='submit' />
            </form>
        </div>
    );
}
export function CreationUI(){
    return(
        <CharSelection /> 
    ); 
}