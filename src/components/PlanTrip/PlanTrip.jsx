import { useState } from "react";
import Sidebar from "../Sidebar/Sidebar";
import "./PlanTrip.css";
import Explore from "../ExplorePage/ExplorePage";

const PlanTrip = () => {
  const [activePanel, setActivePanel] = useState(null);

  const openExplore = () => setActivePanel("explore");
  const openItinerary = () => setActivePanel("itinerary");
  const closeSidebar = () => setActivePanel(null);

  return (
    <div className="plan-trip">
      <h2 className="plan-trip__heading">Plan Your Road Trip</h2>
      <div className="plan-trip__content">
        <Sidebar
          activePanel={activePanel}
          onExploreClick={openExplore}
          onItineraryClick={openItinerary}
          onClose={closeSidebar}
        />
        <Explore />
      </div>
    </div>
  );
};

export default PlanTrip;
