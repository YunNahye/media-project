import './style/LocationButton.css';

function LocationButton({ children, color, onClick }) {
  const classNames = `location-button ${color}`;

  return (
    <div className={classNames} onClick={onClick}>
      {children}
    </div>
  );
}

export default LocationButton;