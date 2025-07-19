// import ExploreForm from "./ExploreForm";
// import Itinerary from "./Itinerary";
import ItineraryIcon from "../../assets/itinerary-icon.png";
import SearchIcon from "../../assets/search-icon.png";
import MapIcon from "../../assets/map-icon.png";
import "./Sidebar.css";

const Sidebar = ({
  activePanel,
  onExploreClick,
  onItineraryClick,
  onClose,
}) => {
  return (
    <div className="sidebar">
      <div className="sidebar__buttons">
        <button className="sidebar__button" onClick={onExploreClick}>
          <img
            src={SearchIcon}
            alt="Explore Icon"
            className="sidebar__button-icon"
          />
          <span>Explore</span>
        </button>
        <button className="sidebar__button" onClick={onItineraryClick}>
          <img
            src={ItineraryIcon}
            alt="Itinerary Icon"
            className="sidebar__button-icon"
          />
          <span>Itinerary</span>
        </button>
        <button className="sidebar__button">
          <img src={MapIcon} alt="Map Icon" className="sidebar__button-icon" />
          <span>Map</span>
        </button>
      </div>

      {/* <div className={`sidebar-panel ${activePanel ? "open" : ""}`}>
        <button className="close-button" onClick={onClose}>
          ×
        </button> */}

      {activePanel === "explore" && <ExploreForm />}
      {activePanel === "itinerary" && <Itinerary />}
    </div>
    // </div>
  );
};

export default Sidebar;
