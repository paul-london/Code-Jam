import "./Featured.css";
import Cards from "../ParkCards/ParkCards";

function Featured() {
  return (
    <div className="featured">
      <div className="featured__container">
        <h2 className="featured__title">Featured National Parks</h2>
        <p className="featured__paragraph">
          Discover some of America's most iconic national parks, each offering
          unique landscapes and unforgettable experiences
        </p>
      </div>
      <Cards />
    </div>
  );
}

export default Featured;
