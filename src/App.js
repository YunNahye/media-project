import './style/App.css';
import React, { useState, useEffect } from 'react';
import Navigation from './Navigation';
import RecycleLabel from './RecycleLabel';
import Cam from './cv/templates';
import io from "socket.io-client";

let endPoint = "http://localhost:5000";
let socket = io.connect(`${endPoint}`)

function App() {
  const [labelColor, setLabelColor] = useState(['gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray']);

  useEffect(() => {
    getMessages();
  }, labelColor);

  const getMessages = () => {
    socket.on("message", msg => {
      const newLabelColor = ['gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'];
      console.log(msg);
      setLabelColor(newLabelColor);
    });
  }

  return (
    <div className="App">
      <Navigation></Navigation>
      <div className="container">
        <div className="webcam-box">
          <Cam/>
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
