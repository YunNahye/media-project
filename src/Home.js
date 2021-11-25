import './style/Home.css';

function Home() {
  return (
    <div className="home">
      <div className="button-box">
        <a href="#" className="button">지도</a>
        <a href="/webcam" className="button">웹캠</a>
      </div>
    </div>
  );
}

export default Home;