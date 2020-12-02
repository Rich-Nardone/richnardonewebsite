
import React, {useState} from 'react'; 
import Slider from '@material-ui/core/Slider';
import Typography from '@material-ui/core/Typography';
import Sound from 'react-sound';
import Grid from '@material-ui/core/Grid';

import VolumeDown from '@material-ui/icons/VolumeDown';
import VolumeUp from '@material-ui/icons/VolumeUp';
import Remove from '@material-ui/icons/Remove';
import Add from '@material-ui/icons/Add';
import AcUnit from '@material-ui/icons/AcUnit';
import Flare from '@material-ui/icons/Flare';


let volu=localStorage.getItem('volume');

let fnt=localStorage.getItem('font');

let bt=localStorage.getItem('borderNum')

let brc=localStorage.getItem('borderColor')



export {fnt};

export {volu};

export {brc};

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

const button_view={
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    
}




export function Options()
{
    //States that will be used to modify the font size, border color, and volume
    
    if(localStorage.getItem('volume') === null)
    {
        const [vol,setVolume]=useState(50);
        localStorage.setItem('volume',vol);
    }
    
    
    if(localStorage.getItem('font') === null)
    {
        const [fontSize,setFontSize]=useState(16);
        localStorage.setItem('font',fontSize);
    }
    
    
    if(localStorage.getItem('borderNum') === null)
    {
        const [borderNum,setBorderNum]=useState(0);
        localStorage.setItem('borderNum',borderNum);
    }
    
    if(localStorage.getItem('borderColor') === null)
    {
        const [borderColor,setBorderColor]=useState('2px solid black')
        localstorage.setItem('borderColor', borderColor)
    }
    
    
    
    const [fontSize, setFontSize]=useState(localStorage.getItem('font'));
    
    const [vol,setVolume]=useState(localStorage.getItem('volume'));
    
    const [font, setFont]=useState(localStorage.getItem('font_style'));
    
    
    const [borderNum, setBorderNum]=useState(localStorage.getItem('borderNum'));
    
    const [borderColor,setBorderColor]=useState(localStorage.getItem('borderColor'));
    
    //==========================================================================
    //DEFAULT STATES FOR SIZES, VOLUME, AND BORDER COLOR IN CASE OF MODIFICATION
    const fS=16;
    const vlme=50;
    const bC=0;
    //===========================================================================
    
    
    function defaultBack(){
        
        setVolume(vlme);
        localStorage.setItem('volume',vlme);
        
        setFontSize(fS);
        localStorage.setItem('font',fS);
        
        setBorderNum(bC)
        localStorage.setItem('borderNum',bC)
        
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
    
    const changeFont = (event, newValue) => 
    {
        setFontSize(newValue);
        localStorage.setItem('font',newValue);
        console.log("Font is now:"+localStorage.getItem('font'));
    }
    
    
    const changeBorderColor = (event, newValue) => 
    {
        
        setBorderNum(newValue);
        localStorage.setItem('borderNum',newValue);
        
        
        if( newValue === 0){
            
            setBorderColor('2px solid black');
            localStorage.setItem('borderColor',borderColor);
            
        }
        
        if( newValue === 1){
            
            setBorderColor('2px solid purple')
            localStorage.setItem('borderColor',borderColor)
            
        }
        
        if( newValue === 2){
            
            setBorderColor('2px solid blue');
            localStorage.setItem('borderColor',borderColor);
            
        }
        
        if( newValue === 3){
            
            setBorderColor('2px solid green');
            localStorage.setItem('borderColor',borderColor);
            
        }
        
        if( newValue === 4){
            
            setBorderColor('2px solid yellow');
            localStorage.setItem('borderColor',borderColor);
            
        }
        
        if( newValue === 5){
            
            setBorderColor('2px solid orange');
            localStorage.setItem('borderColor',borderColor);
            
        }
        
        if( newValue === 6){
            
            setBorderColor('2px solid red');
            localStorage.setItem('borderColor',borderColor);
            
        }
        
        if( newValue === 7){
            
            setBorderColor('2px solid white');
            localStorage.setItem('borderColor',borderColor);
            
        }
        
        console.log("Color is now:"+localStorage.getItem('borderColor'));
    }
    
    
    
    function volume_value(value) {
         return `${value}`;
        }
        
    
    
    const marks = [
    {
        value: 0,
        label: 'Black',
    },
    {
        value: 1,
        label: 'Purple',
    },
    {
        value: 2,
        label: 'Blue',
    },
    {
        value: 3,
        label: 'Green',
    },
    {
        value: 4,
        label: 'Yellow',
    },
    {
        value: 5,
        label: 'Orange',
    },
    {
        value: 6,
        label: 'Red',
    },
    {
        value: 7,
        label: 'White',
    },
    ];
    
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
        <body style= {Volume_style}>
             <Typography style={typography_style} id="fontSize" gutterBottom>
                Font Size
            </Typography>
            <br></br>
            
            <Grid container spacing={2}>
            <Grid item>
            <Remove />
            </Grid>
            <Grid item xs>
            <Slider 
                value={fontSize} 
                onChange={changeFont} 
                aria-labelledby="fontSize"
                valueLabelDisplay="on"
                min={1}
                max={20}
                step={1}
                />
            </Grid>
            <Grid item>
                <Add />
            </Grid>
            </Grid>
            
            
        </body>
        
        <body style= {Volume_style}>
             <Typography style={typography_style} id="borderColor" gutterBottom>
                Border Color
            </Typography>
            <br></br>
            
            <Grid container spacing={2}>
            <Grid item>
            <AcUnit />
            </Grid>
            <Grid item xs>
            <Slider 
                value={borderNum} 
                onChange={changeBorderColor} 
                aria-labelledby="borderColor"
                valueLabelDisplay="off"
                min={0}
                max={7}
                step={1}
                marks={marks}/>
            </Grid>
            <Grid item>
                <Flare />
            </Grid>
            </Grid>
        </body>
        
            <button onClick={defaultBack} style={returnBackButton}> Return to Default Options?</button>
            <button onClick={returnToMain} style={returnBackButton}>Exit Back to Main?</button>
            
        
    
        
      </div>
    );
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}








