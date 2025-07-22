import { useRef } from "react";
import Header from "../Header/Header";
import Main from "../Main/Main";
import Footer from "../Footer/Footer";

function App() {
  const planRef = useRef(null);
  const parksRef = useRef(null);
  const tipsRef = useRef(null);
  const [selectedState, setSelectedState] = useState("");

  const scrollTo = (ref) => {
    if (ref.current) {
      ref.current.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <div className="page">
      <div className="page__content">
        <Header
          onScrollToPlan={() => scrollTo(planRef)}
          onScrollToParks={() => scrollTo(parksRef)}
          onScrollToTips={() => scrollTo(tipsRef)}
        />

        <Main planRef={planRef} parksRef={parksRef} tipsRef={tipsRef} />

        <Footer />
      </div>
    </div>
  );
}

export default App;
