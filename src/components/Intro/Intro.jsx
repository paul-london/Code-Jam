import "./Intro.css";

function Intro() {
  return (
    <div className="intro">
      <div className="intro__container">
        <h1 className="intro__title">Discover America's National Parks</h1>
        <p className="intro__paragraph">
          Plan the ultimate road trip adventure through breathtaking landscapes,
          diverse wildlife, and unforgettable experiences across 50 national
          parks.
        </p>
        <div className="intro__buttons">
          <button className="intro__plan">Plan Your Road Trip</button>
          <button className="intro__explore">Explore Parks</button>
        </div>
      </div>
    </div>
  );
}

export default Intro;
