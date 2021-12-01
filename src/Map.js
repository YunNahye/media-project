import './style/Map.css'
import { useState } from 'react';
import Cam from './cv/templates';
import LocationButton from './LocationButton';
import up from './img/up-arrow_icon.png';
import down from './img/down-arrow_icon.png';

function Map() {
  const [mapType, setMapType] = useState("godeung");
  const [buttonColor, setButtonColor] = useState(["on-focus", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default"]);
  const [slide, setSlide] = useState("button-box");

  const moveSlide = (e) => {
    if (slide == "button-box") {
      setSlide("button-box2")
    }
    else {
      setSlide("button-box")
    }
  }

  const changeMap = (e, place, n) => {
    setMapType(place);
    let newButtonColor = ["default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default", "default"];
    newButtonColor[n] = "on-focus";
    setButtonColor(newButtonColor);
  }

  return(
    <div className="map">
      <div className="container">
        <div className="menu">
          <button onClick={moveSlide}>
            <img className="arrow" src={up}></img>
          </button>
          <div className={slide}>
            <LocationButton color={buttonColor[0]} onClick={(e) => changeMap(e, "godeung", 0)}>고등동</LocationButton>
            <LocationButton color={buttonColor[1]} onClick={(e) => changeMap(e, "gwanggyo1", 1)}>광교1동</LocationButton>
            <LocationButton color={buttonColor[2]} onClick={(e) => changeMap(e, "gwanggyo2", 2)}>광교2동</LocationButton>
            <LocationButton color={buttonColor[3]} onClick={(e) => changeMap(e, "mangpo1", 3)}>망포1동</LocationButton>
            <LocationButton color={buttonColor[4]} onClick={(e) => changeMap(e, "mangpo2", 4)}>망포2동</LocationButton>
            <LocationButton color={buttonColor[5]} onClick={(e) => changeMap(e, "maegyo", 5)}>매교동</LocationButton>
            <LocationButton color={buttonColor[6]} onClick={(e) => changeMap(e, "maetan1", 6)}>매탄1동</LocationButton>
            <LocationButton color={buttonColor[7]} onClick={(e) => changeMap(e, "maetan2", 7)}>매탄2동</LocationButton>
            <LocationButton color={buttonColor[8]} onClick={(e) => changeMap(e, "maetan3", 8)}>매탄3동</LocationButton>
            <LocationButton color={buttonColor[9]} onClick={(e) => changeMap(e, "maetan4", 9)}>매탄4동</LocationButton>
            <LocationButton color={buttonColor[10]} onClick={(e) => changeMap(e, "yeongtong1", 10)}>영통1동</LocationButton>
            <LocationButton color={buttonColor[11]} onClick={(e) => changeMap(e, "yeongtong2", 11)}>영통2동</LocationButton>
            <LocationButton color={buttonColor[12]} onClick={(e) => changeMap(e, "yeongtong3", 12)}>영통3동</LocationButton>
            <LocationButton color={buttonColor[13]} onClick={(e) => changeMap(e, "uman1", 13)}>우만1동</LocationButton>
            <LocationButton color={buttonColor[14]} onClick={(e) => changeMap(e, "uman2", 14)}>우만2동</LocationButton>
            <LocationButton color={buttonColor[15]} onClick={(e) => changeMap(e, "woncheon", 15)}>원천동</LocationButton>
            <LocationButton color={buttonColor[16]} onClick={(e) => changeMap(e, "ingye", 16)}>인계동</LocationButton>
            <LocationButton color={buttonColor[17]} onClick={(e) => changeMap(e, "ji", 17)}>지동</LocationButton>
            <LocationButton color={buttonColor[18]} onClick={(e) => changeMap(e, "haenggung", 18)}>행궁동</LocationButton>
            <LocationButton color={buttonColor[19]} onClick={(e) => changeMap(e, "hwaseo1", 19)}>화서1동</LocationButton>
            <LocationButton color={buttonColor[20]} onClick={(e) => changeMap(e, "hwaseo2", 20)}>화서2동</LocationButton>
          </div>
          <button onClick={moveSlide}>
            <img className="arrow" alt="down_arrow" src={down} />
          </button>
        </div>
        <div className="map-iframe">
          <div className="map-title"><span>종량제 봉투 판매점</span></div>
          <Cam type={mapType} />
        </div>
      </div>
    </div>
  );
}

export default Map;