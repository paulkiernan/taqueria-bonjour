import React from 'react';

import Typography from '@material-ui/core/Typography';

import Header from './components/Header';
import SubscribeDialog from './components/SubscribeDialog';

import './App.css';
import logo from './taco.svg';

export default function App() {
  return (
    <div className="App">
      <Header />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Typography
          variant="h3"
          gutterBottom
          style={{
            fontFamily: 'PermanentMarker',
            marginTop: '7vmin',
          }}
        >
          a forthcoming radical new concept in food
        </Typography>
        <SubscribeDialog />
      </header>
    </div>
  );
}
