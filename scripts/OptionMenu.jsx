
import React, {useState} from 'react'; 
import Slider from '@material-ui/core/Slider';
import Typography from '@material-ui/core/Typography';
import Sound from 'react-sound';
import Grid from '@material-ui/core/Grid';
import VolumeDown from '@material-ui/icons/VolumeDown';
import VolumeUp from '@material-ui/icons/VolumeUp';




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





export function Options()
{
    //States that will be used to modify the font size, border color, and volume
    const [fontSize, setFontSize]=useState(12);
    const [volume,setVolume]=useState(50);
    const [borderColor, setBorderColor]=useState("2px solid black")
    //==========================================================================
    //DEFAULT STATES FOR SIZES, VOLUME, AND BORDER COLOR IN CASE OF MODIFICATION
    const fS=12;
    const vlme=50;
    const bC="2px solid black";
    //===========================================================================
    
    function changeFont(num){
        
        setFontSize(fontSize=num);
        
        
    }
    
    const changeVolume = (event, newValue) => 
    {
        setVolume(newValue);
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
                    volume={volume}
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
                value={volume} 
                onChange={changeVolume} 
                aria-labelledby="slider"
                valueLabelDisplay="on"/>
            </Grid>
            <Grid item>
                <VolumeUp />
            </Grid>
            </Grid>
        </body>
    
        
      </div>
    );
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}








