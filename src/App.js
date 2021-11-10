import './style/App.css';
import Navigation from './Navigation';
import RecycleLabel from './RecycleLabel';

function App() {
  return (
    <div className="App">
      <Navigation></Navigation>
      <div className="container">
        <div className="webcam-box">

        </div>
        <div className="contents">
          <div className="label-box">
            <RecycleLabel color="default">유리</RecycleLabel>
            <RecycleLabel color="default">플라스틱</RecycleLabel>
            <RecycleLabel color="default">종이</RecycleLabel>
            <RecycleLabel color="default">캔</RecycleLabel>
            <RecycleLabel color="default">스티로폼</RecycleLabel>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
