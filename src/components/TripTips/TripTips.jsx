import { useState } from "react";
import "./TripTips.css";

function Tips() {
  const [activeTab, setActiveTab] = useState("Planning");

  return (
    <div className="tips">
      <div className="tips__container">
        <h2 className="tips__title">Essential Travel Tips</h2>
        <p className="tips__paragraph">
          Make the most of your national park road trip with expert advice on
          planning, packing, and staying safe.
        </p>

        <div className="tips__tabs">
          {["Planning", "Packing", "Safety"].map((tab) => (
            <button
              key={tab}
              className={`tips__tab ${activeTab === tab ? "active" : ""}`}
              onClick={() => setActiveTab(tab)}
            >
              {tab}
            </button>
          ))}
        </div>

        <div className="tips__info">
          {activeTab === "Planning" && (
            <div className="tips__grid">
              <div className="tip__card">
                <h4>📅 Book Accommodations Early</h4>
                <p>
                  Popular parks fill up months in advance, especially during
                  peak season.
                </p>
              </div>
              <div className="tip__card">
                <h4>📍 Research Seasonal Closures</h4>
                <p>
                  Some roads and trails close seasonally due to weather
                  conditions.
                </p>
              </div>
              <div className="tip__card">
                <h4>🎟️ Check Park Passes</h4>
                <p>
                  Annual America the Beautiful pass pays for itself after
                  visiting 3+ parks.
                </p>
              </div>
              <div className="tip__card">
                <h4>📶 Plan for Cell Service</h4>
                <p>
                  Download offline maps and inform others of your itinerary.
                </p>
              </div>
            </div>
          )}

          {activeTab === "Packing" && (
            <div className="tips__grid">
              <div className="tip__card">
                <h4>🚗 Vehicle Essentials</h4>
                <ul>
                  <li>Spare tire & tools</li>
                  <li>Jumper cables</li>
                  <li>Emergency kit</li>
                  <li>Water & snacks</li>
                  <li>Paper maps</li>
                </ul>
              </div>
              <div className="tip__card">
                <h4>🥾 Hiking & Outdoor</h4>
                <ul>
                  <li>Comfortable hiking boots</li>
                  <li>Layered clothing</li>
                  <li>Sun protection</li>
                  <li>First aid kit</li>
                  <li>Headlamp/flashlight</li>
                </ul>
              </div>
              <div className="tip__card">
                <h4>📸 Photography Gear</h4>
                <ul>
                  <li>Camera & extra batteries</li>
                  <li>Tripod for landscapes</li>
                  <li>Lens cleaning kit</li>
                  <li>Memory cards</li>
                  <li>Portable charger</li>
                </ul>
              </div>
              <div className="tip__card">
                <h4>🗺️ Park Specific</h4>
                <ul>
                  <li>Park maps & guides</li>
                  <li>Binoculars for wildlife</li>
                  <li>Reusable water bottle</li>
                  <li>Weather appropriate gear</li>
                  <li>Cash for fees</li>
                </ul>
              </div>
            </div>
          )}

          {activeTab === "Safety" && (
            <div className="tips__grid">
              <div className="tip__card high-priority">
                <h4>
                  🦌 Wildlife Safety{" "}
                  <span className="priority">High Priority</span>
                </h4>
                <p>
                  Keep a safe distance from all wildlife. Store food properly to
                  avoid attracting animals.
                </p>
              </div>
              <div className="tip__card high-priority">
                <h4>
                  🌦️ Weather Preparedness{" "}
                  <span className="priority">High Priority</span>
                </h4>
                <p>
                  Mountain weather can change rapidly. Check conditions and
                  dress in layers.
                </p>
              </div>
              <div className="tip__card medium-priority">
                <h4>
                  🥾 Hiking Safety{" "}
                  <span className="priority">Medium Priority</span>
                </h4>
                <p>
                  Tell someone your plans, carry water, and know your limits.
                </p>
              </div>
              <div className="tip__card medium-priority">
                <h4>
                  🚙 Vehicle Maintenance{" "}
                  <span className="priority">Medium Priority</span>
                </h4>
                <p>
                  Check your vehicle before long drives. Keep gas tank full in
                  remote areas.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Tips;
