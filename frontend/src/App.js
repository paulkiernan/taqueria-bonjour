import React, { useEffect } from 'react';

import Typography from '@material-ui/core/Typography';

import Header from './components/Header';
import SubscribeDialog from './components/SubscribeDialog';
import { initGA, PageView } from './components/Tracking';

import './App.css';
import logo from './media/taco.svg';

initGA('UA-41647925-5');

const App = () => {
  useEffect(() => {
    PageView();
  });

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
};

export default App;
