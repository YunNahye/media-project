import './style/RecycleLabel.css';

function RecycleLabel({ children, color }) {
  const classNames = `label ${color}`;

  return (
    <div className={classNames}>
      {children}
    </div>
  );
}

export default RecycleLabel;