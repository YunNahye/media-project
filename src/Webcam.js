import './style/Webcam.css';
import React, { useState, useEffect } from 'react';
import ImgBox from './ImgBox';
import Cam from './cv/templates';
import io from 'socket.io-client';

let endPoint = "http://localhost:5000";
let socket = io.connect(`${endPoint}`)

function Webcam() {
  const recycleType = ['pet', 'bone', 'brown_glass', 'can', 'clothes', 'green_glass', 'husk', 'newspaper', 'paperbox', 'paperpack', 'seed', 'styrofoam', 'vinyl'];
  const [imgType, setImgType] = useState("pet");
  
  useEffect(() => {
    getMessages();
  }, [imgType]);

  const getMessages = () => {
    socket.on("message", msg => {
        setImgType(recycleType[msg]);
    });
  }

  return (
    <div className="Webcam">
      <div className="page-name">
        분리수거 도우미
      </div>
      <div className="container">
        <div className="webcam-box">
          <div className="camera">
            <Cam type="cam"/>
          </div>
        </div>
        <div className="contents">
          <ImgBox imgType={imgType}></ImgBox>
        </div>
      </div>
    </div>
  );
}

export default Webcam;