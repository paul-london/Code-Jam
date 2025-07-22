import PlanTrip from "../PlanTrip/PlanTrip";
import Featured from "../Featured/Featured";
import Tips from "../TripTips/TripTips";

function Main({ planRef, parksRef, tipsRef, selectedState, setSelectedState }) {
  return (
    <main className="main">
      <section ref={planRef} id="plan">
        <PlanTrip />
      </section>

      <section ref={parksRef} id="parks">
        <Featured />
      </section>

      <section ref={tipsRef} id="tips">
        <Tips />
      </section>
    </main>
  );
}

export default Main;
