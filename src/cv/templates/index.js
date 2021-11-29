import React, { useState } from "react";

function Cam({ type }) {
  const typeSrc = `http://localhost:5000/${ type }`;
  if (type == "rhkdry") {
    return (
      <div>
      <iframe
        src={typeSrc}
      />
      </div>
    );
  }
};

export default Cam;
