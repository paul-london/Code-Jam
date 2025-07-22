import "./ExplorePage.css";

function Explore({
  onClose,
  onStateSelected,
  selectedState,
  setSelectedState,
}) {
  const handleSubmit = (e) => {
    e.preventDefault();
    if (selectedState) {
      onStateSelected(selectedState);
    }
  };

  return (
    <div className="explore">
      <button onClick={onClose} className="explore__close-btn">
        &times;
      </button>
      <h4 className="explore__title">
        Are you ready for the adventure of a life time?
      </h4>
      <p className="explore__paragraph">
        Pack your bags, fill up your gas tank and lets go!!
      </p>
      <div className="explore__container">
        <form action="" className="explore__form" onSubmit={handleSubmit}>
          <label htmlFor="state" className="explore__label">
            Choose a State:
          </label>
          <select
            id="state"
            name="state"
            className="explore__input"
            value={selectedState}
            onChange={(e) => setSelectedState(e.target.value)}
          >
            <option value="">-- Select a state --</option>
            <option value="CA">Califonia</option>
            <option value="FL">Florida</option>
            <option value="KS">Kansas</option>
            <option value="NY">New York</option>
            <option value="PA">Pennsylvania</option>
            <option value="VA">Virginia</option>
          </select>
          <button type="submit" className="explore__submit-btn">
            Go
          </button>
        </form>
        <div className="explore__car-animation">
          <img src="src/assets/car.jpeg" alt="Driving car" className="car" />
        </div>
      </div>
    </div>
  );
}

export default Explore;
