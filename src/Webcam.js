import './style/Webcam.css';
import React, { useState, useEffect } from 'react';
import RecycleLabel from './RecycleLabel';
import Cam from './cv/templates';
import io from "socket.io-client";

let endPoint = "http://localhost:5000";
let socket = io.connect(`${endPoint}`)

function Webcam() {
  const [labelColor, setLabelColor] = useState(['default', 'default', 'default', 'default', 'default', 'default', 'default', 'default', 'default', 'default', 'default', 'default']);

  useEffect(() => {
    getMessages();
  }, labelColor);

  const getMessages = () => {
    socket.on("message", msg => {
      const newLabelColor = ['default', 'default', 'default', 'default', 'default', 'default', 'default', 'default', 'default', 'default', 'default', 'default'];
      newLabelColor[msg] = 'on-focus';
      setLabelColor(newLabelColor);
    });
  }

  return (
    <div className="Webcam">
      <div className="container">
        <div className="webcam-box">
          <div className="camera">
            <Cam type="cam"/>
          </div>
          <div className="label"></div>
        </div>
        <div className="contents">
          <div className="main-img"></div>
          {/* <div className="label-box">
            <RecycleLabel color={labelColor[0]}>plastic</RecycleLabel>
            <RecycleLabel color={labelColor[1]}>brown_glass</RecycleLabel>
            <RecycleLabel color={labelColor[2]}>can</RecycleLabel>
            <RecycleLabel color={labelColor[3]}>cloth</RecycleLabel>
            <RecycleLabel color={labelColor[4]}>green_glass</RecycleLabel>
            <RecycleLabel color={labelColor[5]}>newspaper</RecycleLabel>
            <RecycleLabel color={labelColor[6]}>paperbox</RecycleLabel>
            <RecycleLabel color={labelColor[7]}>paperpack</RecycleLabel>
            <RecycleLabel color={labelColor[8]}>styrofoam</RecycleLabel>
            <RecycleLabel color={labelColor[9]}>vinyl</RecycleLabel>
            <RecycleLabel color={labelColor[10]}>white_glass</RecycleLabel>
            <RecycleLabel color={labelColor[11]}>else</RecycleLabel>
          </div> */}
        </div>
      </div>
    </div>
  );
}

export default Webcam;