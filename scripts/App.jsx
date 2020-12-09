import React from 'react';
import Sound from 'react-sound';
import { EmailLogin } from './EmailLogin';
import { GoogleLoginButton } from './GoogleButton';

const h1 = {
  textAlign: 'center',
  padding: 50,
  margin: 50,
  fontWeight: 'bold',
  fontStyle: 'italic',
  borderWidth: 5,
  background: 'grey',
  borderRadius: 10,
  boxShadow: '2px 5px black',
};

export function App() {
  return (
    <div>
      <h1 style={h1}>Welcome to Text RPG</h1>

      <hr />
      <GoogleLoginButton />
      <br />
      <EmailLogin />
      <Sound
        url="/static/Login.mp3"
        playStatus={Sound.status.PLAYING}
        volume="50"
      />
      <hr />
    </div>

  );
}

export default App;
