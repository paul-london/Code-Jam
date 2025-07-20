import { useState } from "react";
import Sidebar from "../Sidebar/Sidebar";
import Explore from "../ExplorePage/ExplorePage";
import Itinerary from "../Itinerary/Itinerary";
import "./PlanTrip.css";

const PlanTrip = () => {
  const [activePanel, setActivePanel] = useState("");
  const [showExplore, setShowExplore] = useState(false);
  const [showItinerary, setShowItinerary] = useState(false);

  const openExplore = () => {
    setShowExplore(true);
    setShowItinerary(false);
    setActivePanel("explore");
  };

  const openItinerary = () => {
    setShowItinerary(true);
    setShowExplore(false);
    setActivePanel("itinerary");
  };

  const closeSidebar = () => {
    setActivePanel("");
    setTimeout(() => {
      setShowExplore(false);
      setShowItinerary(false);
    }, 200);
  };

  return (
    <div className="plan-trip">
      <h2 className="plan-trip__heading">Plan Your Road Trip</h2>
      <div className="plan-trip__content">
        <Sidebar
          activePanel={activePanel}
          onExploreClick={openExplore}
          onItineraryClick={openItinerary}
        />

        {showExplore && (
          <div
            className={`explore-panel ${
              activePanel === "explore" ? "explore-panel--open" : ""
            }`}
          >
            <Explore onClose={closeSidebar} />
          </div>
        )}

        {showItinerary && (
          <div
            className={`itinerary-panel ${
              activePanel === "itinerary" ? "itinerary-panel--open" : ""
            }`}
          >
            <Itinerary onClose={closeSidebar} />
          </div>
        )}
      </div>
    </div>
  );
};

export default PlanTrip;
