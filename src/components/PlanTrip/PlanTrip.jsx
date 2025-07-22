import { useState } from "react";
import Sidebar from "../Sidebar/Sidebar";
import Explore from "../ExplorePage/ExplorePage";
import Itinerary from "../Itinerary/Itinerary";
import MapView from "../Map/MapView";
import "./PlanTrip.css";

const PlanTrip = () => {
  const [activePanel, setActivePanel] = useState("");
  const [showExplore, setShowExplore] = useState(false);
  const [showItinerary, setShowItinerary] = useState(false);
  const [selectedState, setSelectedState] = useState("");
  const [route, setRoute] = useState([]);

  const handleStateSelected = (stateCode) => {
    console.log("Selected State:", stateCode);
    setSelectedState(stateCode);
  };

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
            <Explore
              onClose={closeSidebar}
              selectedState={selectedState}
              setSelectedState={setSelectedState}
              onStateSelected={handleStateSelected}
            />
          </div>
        )}

        {showItinerary && (
          <div
            className={`itinerary-panel ${
              activePanel === "itinerary" ? "itinerary-panel--open" : ""
            }`}
          >
            <Itinerary onClose={closeSidebar} route={route} />
          </div>
        )}

        <MapView
          selectedState={selectedState}
          route={route}
          setRoute={setRoute}
        />
      </div>
    </div>
  );
};

export default PlanTrip;
