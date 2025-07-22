import Navigation from "../Navigation/Navigation";
import Intro from "../Intro/Intro";

function Header({ onScrollToPlan, onScrollToParks, onScrollToTips }) {
  return (
    <header className="header">
      <Navigation
        onScrollToPlan={onScrollToPlan}
        onScrollToParks={onScrollToParks}
        onScrollToTips={onScrollToTips}
      />
      <Intro />
    </header>
  );
}

export default Header;
