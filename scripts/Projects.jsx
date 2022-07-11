import React from 'react';
import { NavBar } from './NavBar';
import { volu, fnt, brc } from './OptionMenu';

const button = {
  position: 'relative',
  fontWeight: 'bold',
  fontStyle: 'italic',
  width: 210,
  border: brc,
  fontSize: fnt,
  top: 300,
  borderRadius: 10,
};

const div ={
    fontStyle:'bold',
    fontSize:32,
    marginLeft: 'auto',
    marginRight: 'auto',
    verticalAlign: 'middle',
    width: '800px',
    display: 'block',
}
const resumeOutline = {
    position: 'relative',
    fontWeight: 'bold',
    fontStyle: 'italic',
    backgroundColor: 'white',
    fontColor: 'black',
    float: 'left',
    clear: 'left',
  };
 const h = {
    textAlign:'center'
 }

export function Projects() {

  return (
    <div>
      <NavBar />
      <div style={div}>
        <br />
        <h2 style={h}>Projects</h2>
        <br />
        <p>Created a Convolutional Neural Network to classify retinal optical coherence tomography images for four diseases to 95% accuracy. Used a database of 80,000+ Retinal OCTs to train and validate the Network. <a href='https://github.com/Rich-Nardone/NeurelNetwork'>View here</a></p>
        <p>Implemented Random Forest Classifier with Python and performed feature engineering to predict Titanic Survival to a 78% accuracy. <a href='https://github.com/Rich-Nardone/Titanic/blob/main/CS675%20Final%20Project.ipynb'>View here</a></p>
        <p>Developed a web scraping tool in Python to pull heart rate monitor data from websites and export specific data to excel sheets for coaches. <a href='https://github.com/Rich-Nardone/ExtractPolarDATA'>View here</a></p>
        <p>Created a Text-RPG game for a capstone project using python flask app and React. <a href='https://github.com/Rich-Nardone/CS490-Text-RPG'>View here</a></p>
        <p>Developed a portfolio website using flask and react to display achievements and projects. <a href='https://github.com/Rich-Nardone/richnardonewebsite'>View here</a></p>
      </div>
    </div>
  );
}

export default Projects;
