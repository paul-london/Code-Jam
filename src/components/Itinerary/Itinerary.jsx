import "./Itinerary.css";

const parks = [
  {
    id: 1,
    name: "Mount Revelstoke National Park",
    location: "BC",
    image: "https://via.placeholder.com/100x60?text=Park+1",
    miles: 30,
    time: "32m",
  },
  {
    id: 2,
    name: "The Enchanted Forest",
    location: "BC",
    image: "https://via.placeholder.com/100x60?text=Park+2",
    miles: 22,
    time: "22m",
  },
  {
    id: 3,
    name: "Sicamous KOA",
    location: "BC",
    image: "https://via.placeholder.com/100x60?text=Park+3",
    miles: 2,
    time: "2m",
  },
  {
    id: 4,
    name: "D Dutchman Dairy",
    location: "BC",
    image: "https://via.placeholder.com/100x60?text=Park+4",
    miles: 19,
    time: "21m",
  },
];

function Itinerary({ onClose }) {
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
            {index !== parks.length - 1 && <div className="timeline__line" />}
          </div>

          <div className="timeline__card">
            <img src={park.image} alt={park.name} className="timeline__image" />
            <div className="timeline__info">
              <h4 className="timeline__park-name">{park.name}</h4>
              <p className="timeline__location">{park.location}</p>
              <div className="timeline__details">
                <span>{park.miles} mi</span>
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
