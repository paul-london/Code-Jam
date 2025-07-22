import Logo from "../../assets/Logo.png";
import "./Navigation.css";

function Navigation({ onScrollToPlan, onScrollToParks, onScrollToTips }) {
  return (
    <nav className="nav">
      <div className="nav__container">
        <div className="nav__logo">
          <img src={Logo} alt="logo" className="nav__image" />
          <p className="nav__title">Park Hopper Routes</p>
        </div>
        <ul className="nav__links">
          <li onClick={onScrollToPlan} className="nav__plan">
            Plan a Trip
          </li>
          <li onClick={onScrollToParks} className="nav__parks">
            Parks
          </li>
          <li onClick={onScrollToTips} className="nav__tips">
            Travel Tips
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navigation;
