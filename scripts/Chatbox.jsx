import React, {useState, useEffect} from 'react'; 
import {Socket} from './Socket.jsx';
export function Chatbox(){
    const [userInput, setInput] = useState("");
    const [chatLog, setLog] = useState([]);
    
    function submitInput(event){
        event.preventDefault();
        Socket.emit('user input', {'input': userInput});
        document.getElementById('user_text_box').value = ""
    }
    
    function retrieve_chatlog(){
        useEffect(()=>{
           Socket.on('user chatlog', (data)=>{
               setLog(data);
           }); 
        });    
    }
    const display_log = chatLog.map((log,index)=>
        <li key={index}> {log} </li>
    );
    retrieve_chatlog();
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