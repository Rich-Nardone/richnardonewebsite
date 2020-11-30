
import React, {useState} from 'react'; 
import Slider from '@material-ui/core/Slider';
import Typography from '@material-ui/core/Typography';
import Sound from 'react-sound';
import Grid from '@material-ui/core/Grid';
import VolumeDown from '@material-ui/icons/VolumeDown';
import VolumeUp from '@material-ui/icons/VolumeUp';


let volu=localStorage.getItem('volume');

export {volu};


const h1={
    
    color:'white',
    textAlign: 'center',
    padding: 50,
    margin: 50,
    fontWeight: 'bold',
    borderWidth: 5,
    background: 'linear-gradient(green,bluegreen)',
    borderRadius:10,
    
};
const typography_style={
    
    color:'white',
    fontSize:25,
    textAlign: 'center',
    fontWeight:'bold',
    
    
}
const Volume_style={
    background: 'linear-gradient(green,green)',
    borderRadius:10,
    border:'2px solid black',
    
}

const returnBackButton={
    textAlign:'center',
    fontWeight:'bold',
    fontStyle:'italic',
    background: 'linear-gradient(green,green)',
    padding: 5,
    margin: 5,
    borderRadius:10,
    fontSize:18,
    width:1500,
    
};





export function Options()
{
    //States that will be used to modify the font size, border color, and volume
    const [fontSize, setFontSize]=useState(12);
    if(localStorage.getItem('volume') === null)
    {
        const [vol,setVolume]=useState(50);
        localStorage.setItem('volume',vol)
    }
    
    const [vol,setVolume]=useState(localStorage.getItem('volume'));
    
    
    const [borderColor, setBorderColor]=useState("2px solid black");
    //==========================================================================
    //DEFAULT STATES FOR SIZES, VOLUME, AND BORDER COLOR IN CASE OF MODIFICATION
    const fS=12;
    const vlme=50;
    const bC="2px solid black";
    //===========================================================================
    
    function changeFont(num){
        
        setFontSize(fontSize=num);
        
        
    }
    
    function defaultBack(){
        
        setVolume(vlme);
        localStorage.setItem('volume',vlme)
        
        setFontSize(fS);
        
        setBorderColor(bC);
    }
    
    function returnToMain(){
        
        return(window.location = "main_chat.html")
    }
    
    const changeVolume = (event, newValue) => 
    {
        setVolume(newValue);
        localStorage.setItem('volume',newValue);
        console.log("Volume is now:"+localStorage.getItem('volume'));
    }
    
    
    function volume_value(value) {
         return `${value}`;
        }
        
    function changeBorderColor(color){
        
        setBorderColor(borderColor="2px solid "+color);
        
    }
    
    return(
      <div>
        <Sound
                    url='/static/options_bm.mp3'
                    playStatus={Sound.status.PLAYING}
                    volume={vol}
            />
        
        <h1 style={h1}>OPTIONS</h1>
        
        <body style={Volume_style}>    
           <Typography style={typography_style} id="slider" gutterBottom>
            Volume
            </Typography>
            <br></br>
            
            <Grid container spacing={2}>
            <Grid item>
            <VolumeDown />
            </Grid>
            <Grid item xs>
            <Slider 
                value={vol} 
                onChange={changeVolume} 
                aria-labelledby="slider"
                valueLabelDisplay="on"/>
            </Grid>
            <Grid item>
                <VolumeUp />
            </Grid>
            </Grid>
        </body>
        
            <button onClick={defaultBack} style={returnBackButton}> Return to Default Options?</button>
            <button onClick={returnToMain} style={returnBackButton}>Exit Back to Main?</button>
            
        
    
        
      </div>
    );
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}








