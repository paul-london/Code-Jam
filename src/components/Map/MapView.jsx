// import {
//   MapContainer,
//   TileLayer,
//   Marker,
//   Popup,
//   Polyline,
// } from "react-leaflet";
// import L from "leaflet";
// import "leaflet/dist/leaflet.css";
import { useState, useEffect } from "react";
import "./MapView.css";

// const greenIcon = new L.Icon({
//   iconUrl:
//     "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png",
//   iconSize: [25, 41],
//   iconAnchor: [12, 41],
// });

// function MapView() {
//   const positions = [
//     {
//       coords: [36.778261, -119.417932],
//       popup: "Start: CA",
//     },
//     {
//       coords: [37.85982543, -122.6007386],
//       popup: "Golden Gate National Recreation Area",
//     },
//     // ... add other locations
//   ];

//   const polylinePaths = [
//     [
//       [36.778261, -119.417932],
//       [37.85982543, -122.6007386],
//     ],
//     // ... add other paths
//   ];

//   return (
//     <MapContainer center={[39, -98]} zoom={4} className="map">
//       <TileLayer url="https://tile.openstreetmap.org/{z}/{x}/{y}.png" />
//       {positions.map((pos, index) => (
//         <Marker key={index} position={pos.coords} icon={greenIcon}>
//           <Popup>{pos.popup}</Popup>
//         </Marker>
//       ))}
//       {polylinePaths.map((path, idx) => (
//         <Polyline key={idx} positions={path} color="blue" />
//       ))}
//     </MapContainer>
//   );
// }

// export default MapView;

function MapView({ selectedState }) {
  const [loading, setLoading] = useState(true);

  let mapFile = "blank_us_map.html";

  if (selectedState === "CA") {
    mapFile = "usa_roadtrip_map_CA.html";
  } else if (selectedState === "VA") {
    mapFile = "usa_roadtrip_map_VA.html";
  } else if (selectedState === "FL") {
    mapFile = "usa_roadtrip_map_FL.html";
  } else if (selectedState === "NY") {
    mapFile = "usa_roadtrip_map_NY.html";
  } else if (selectedState === "KS") {
    mapFile = "usa_roadtrip_map_KS.html";
  } else if (selectedState === "PA") {
    mapFile = "usa_roadtrip_map_PA.html";
  }

  useEffect(() => {
    setLoading(true); // show spinner right away on state change

    const timer = setTimeout(() => {
      setLoading(false); // hide spinner after 5 seconds
    }, 8000);

    return () => clearTimeout(timer); // clean up if user switches states quickly
  }, [selectedState]);

  return (
    <div>
      {loading && (
        <div className="spinner-overlay">
          <div className="spinner" />
          <p className="spinner__paragraph">Fetching Route...</p>
          <img src="src/assets/car.jpeg" alt="Driving car" className="car" />
        </div>
      )}

      <div className="map">
        <iframe
          title="Folium Map"
          src={`${import.meta.env.BASE_URL}maps/${mapFile}`}
          style={{ width: "100%", height: "100%", border: "none" }}
          onLoad={() => setLoading(false)}
        />
      </div>
    </div>
  );
}

// export default MapView;

// import {
//   MapContainer,
//   TileLayer,
//   Marker,
//   Polyline,
//   Popup,
// } from "react-leaflet";
// import "./MapView.css";

// function MapView({ route }) {
//   const positions = route.map((park) => [park.lat, park.lng]);

//   return (
//     <MapContainer center={[37, -95]} zoom={4} className="map">
//       <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

//       {route.map((park) => (
//         <Marker key={park.id} position={[park.lat, park.lng]}>
//           <Popup>{park.name}</Popup>
//         </Marker>
//       ))}

//       {positions.length > 1 && <Polyline positions={positions} color="blue" />}
//     </MapContainer>
//   );
// }
export default MapView;
