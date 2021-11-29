import './style/Map.css'
import Cam from './cv/templates';
import RecycleLabel from './RecycleLabel';

function Map() {
  return(
    <div className="map">
      <div className="container">
        <div className="label-box">
          <RecycleLabel color='default'>광교1동</RecycleLabel>
        </div>
        <div className="map-iframe">
          <Cam type='rhkdry' />
        </div>
      </div>
    </div>
  );
}

export default Map;