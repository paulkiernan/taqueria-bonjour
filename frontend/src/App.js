import { Helmet } from 'react-helmet'

import logo from './taco.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <Helmet>
        <meta charSet="utf-8" />
        <title>Taqueria Bonjour</title>
        <link rel="canonical" href="http://bonjour.paulynomial.com/" />
      </Helmet>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p
          className="App-link"
        >
          a forthcoming radical new concept in food
        </p>
      </header>
    </div>
  );
}

export default App;
