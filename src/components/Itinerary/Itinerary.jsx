import "./Itinerary.css";
import parks from "../../contexts/parksData";

function Itinerary({ onClose, route }) {
  return (
    <div className="timeline">
      <div className="timeline__header">
        <button onClick={onClose} className="timeline__close-btn">
          &times;
        </button>
      </div>

      <h2 className="timeline__title">Itinerary</h2>

      {parks.map((park, index) => (
        <div className="timeline__item" key={park.id}>
          <div className="timeline__indicator">
            <div className="timeline__number">{index + 1}</div>
            {index !== route.length - 1 && <div className="timeline__line" />}
          </div>

          <div className="timeline__card">
            <img
              src={park.image_url}
              alt={park.name}
              className="timeline__image"
            />
            <div className="timeline__info">
              <h4 className="timeline__park-name">{park.name}</h4>
              <p className="timeline__location">{park.location}</p>
              <div className="timeline__details">
                <span>{park.miles}</span>
                <span>{park.time}</span>
              </div>
            </div>
            <div className="timeline__expand">⌄</div>
          </div>
        </div>
      ))}
    </div>
  );
}
export default Itinerary;
