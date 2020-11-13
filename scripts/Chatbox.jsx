import React, {useState, useEffect} from 'react'; 
import {Socket} from './Socket.jsx';

export function Chatbox(props){
    const [userInput, setInput] = useState("");
    
    function submitInput(event){
        event.preventDefault();
        Socket.emit('user input', {'input': userInput});
        document.getElementById('user_text_box').value = "";
    }
    const display_log = props.user_content.map((log,index)=>
        <li key={index}> {log} </li>
    );
    
    return(
        <div>
            <div id='chatbox'>
                <ul>
                    {display_log}
                </ul>
            </div> 
            
            <div id='user_buttons'>
                <form onSubmit={submitInput}>
                    <input id='user_text_box' type='text' placeholder='What is your command?' onChange={e=>setInput(e.target.value)}/>
                    <input type='submit' /> 
                </form>
            </div>
        </div>
    )
}