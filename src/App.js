import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navigation from './Navigation';
import Webcam from './Webcam';
import Map from './Map';

function App() {
  return (
    <div>
      <Navigation></Navigation>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Webcam />}/>
          <Route path="/map" element={<Map />}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
