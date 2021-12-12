import './style/ImgBox.css';

function ImgBox({ imgType }) {
  const classNames = `img-box ${imgType}`;

  return(
    <div className={classNames}>

    </div>
  );
}

export default ImgBox;