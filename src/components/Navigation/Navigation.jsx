import Logo from "../../assets/Logo.png";
import "./Navigation.css";

function Navigation() {
  return (
    <nav className="nav">
      <div className="nav__container">
        <div className="nav__logo">
          <img src={Logo} alt="Park Hopper Logo" className="nav__image" />
          <p className="nav__title">Park Hopper Routes</p>
        </div>
        <ul className="nav__links">
          <li className="nav__plan">
            <a href="/map" className="nav__link">
              Plan a Trip
            </a>
          </li>
          <li className="nav__parks">
            <a href="/parks" className="nav__link">
              Parks
            </a>
          </li>
          <li className="nav__tips">
            <a href="/tips" className="nav__link">
              Travel Tips
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navigation;
