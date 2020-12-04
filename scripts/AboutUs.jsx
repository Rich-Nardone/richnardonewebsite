import React from 'react'; 


export function About(){
    
    function toLogin(event){
       return window.location = "login.html"
    }
    
    return(
        <div>
            <h1> Welcome to Text RPG </h1> 
            <p> About Us </p> 
            <ul>
                <li>Who we are</li>
                <p> [Enter info here] </p> 
                <li>What we made and what it does </li> 
                <p> [Enter info here] </p> 
                <li>How you made it and what technologies were used</li>
                <p> [Enter info here] </p> 
                <li> Why you've amde it and why it matters </li> 
                <p> [Enter info here] </p> 
            </ul>
            
            <button onClick = {toLogin}> Enter Website </button> 
        </div>
    )
}