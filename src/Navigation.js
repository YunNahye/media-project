import './style/Navigation.css';
import mapMarker from './img/map-marker.png';
import camera from './img/camera.png';

function Navigation(){
  return (
    <div className="navbar">
      <div className="logo">
        <span>DDOK-DDOK</span>
      </div>
      <div className="map-button">
        <a href="/map"><img className="marker" src={mapMarker} /><span className="marker-name">Map</span></a>
        <a href="/"><img className="marker" src={camera} /><span className="marker-name">Cam</span></a>
      </div>
    </div>
  );
}

export default Navigation;