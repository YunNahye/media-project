import './style/RecycleLabel.css';

function RecycleLabel({ children, color, onClick }) {
  const classNames = `label ${color}`;

  return (
    <div className={classNames} onClick={onClick}>
      {children}
    </div>
  );
}

export default RecycleLabel;