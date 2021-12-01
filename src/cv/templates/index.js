import React, { useState } from "react";

function Cam({ type }) {
  const typeSrc = `http://localhost:5000/${ type }`;
  if (type == "rhkdry") {
    return (
      <div>
        <img src={typeSrc} alt="Video" />
      </div>
    );
  }
  else {
    return (
      <div>
        <iframe src={typeSrc}></iframe>
      </div>
    );
  }
};

export default Cam;
