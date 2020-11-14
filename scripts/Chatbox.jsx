import React, {useState} from 'react'; 
import {Socket} from './Socket.jsx';
import PropTypes from 'prop-types';


const div={
    width:1000,
    height:406,
    position: 'fixed',
    left:214.5,
    top:8,
    display: 'inline',
    background:'grey',
    border:'3px solid black',
    
}
const ul={
    listStyleType:'none',
    height: 310,
    textAlign:'left',
    overflow: 'scroll',
    fontStyle:'italic',
    fontWeight: "bold",
   
};

const input={
    
    width:942,
}
const p={
    
    padding:0,
    margin:0,
    position: 'relative',
    border:'2px solid black',
    fontWeight:'bold',
    textAlign:'center',
    opacity: 0.5,
    fontStyle:'italic',
    
    
}

const secret_p={
    textAlign:'center',
    fontWeight:'bold',
    fontStyle:'italic',
    background:'grey',
    
    
    
    
}

const details={
    fontWeight:'bold',
    textAlign:'center',
    fontStyle:'italic',
}

const body={
    background:'grey',
}


export function Chatbox(props){
    const [userInput, setInput] = useState("");
    const[money,setMoney] = useState(1000);
    
    function submitInput(event){
        event.preventDefault();
        Socket.emit('user input', {'input': userInput});
        document.getElementById('user_text_box').value = "";
    }
    const display_log = props.user_content.map((log,index)=>
        <li key={index}> {log} </li>
    );
    
    function submitPayment(){
        if(money===0){
            setMoney(0)
        }
        else{
        setMoney(money-500)
        Socket.emit('item purchased')
        }
    }
    
    return(
        <div style={div}>
            <div id='chatbox'>
                <ul style={ul}>
                    {display_log}
                </ul>
            </div> 
            <p style={p}>{'Possible Actions: "Say", "Do", "Attack"'}</p>
            <details>
                <summary style={details}>Pssst..click me for goods</summary>
                <body style={body}>
                <p style={secret_p}> {"Welcome to Ghosty's Emporium! What can I get ye?"}</p>
                <p style={secret_p}>Current Money: {money} Bucks</p>
                <br></br>
                <button id='Health' onClick={submitPayment}>Health Pack: 500 Bucks</button>
                </body>
                
            </details>
            <br></br>
            <div id='user_buttons'>
                <form onSubmit={submitInput}>
                    <input style={input} id='user_text_box' type='text' placeholder='What is your command?' onChange={e=>setInput(e.target.value)}/>
                    <input type='submit' /> 
                </form>
            </div>
        </div>
    )
}

Chatbox.propTypes = {
    user_content: PropTypes.array,
};