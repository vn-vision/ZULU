import logo from './assets/images/logo.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to Zulu RE<br/>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p> This is the main src app, Call components to display them...</p>
      </header>
    </div>
  );
}

export default App;
