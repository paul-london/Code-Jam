import "./ParkCards.css";

function Cards() {
  return (
    <div className="cards">
      <ul className="cards__container">
        <li className="card">
          <img
            src="/Park-Hopper-Routes/images/parkimages/Golden_Gate_National_Recreation_Area.jpg"
            alt="Golden Gate National Recreation Area"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Golden Gate National Recreation Area</h3>
              <span className="card__badge">🗓️ May - October</span>
            </div>

            <p className="card__location">📍 San Franciso, Califonia</p>

            <p className="card__description">
              Experience a park so rich it supports 19 distinct ecosystems with
              over 2,000 plant and animal species. Go for a hike, enjoy a vista,
              have a picnic or learn about the centuries of overlapping history
              from California's indigenous cultures, Spanish colonialism,
              the Mexican Republic, US military expansion and the growth of San
              Francisco. All of this and more awaits you, so get out and find
              your park.
            </p>

            <div className="card__highlights">
              <span className="highlight">Iconic Landmarks</span>
              <span className="highlight">Scenic Coastal Areas</span>
              <span className="highlight">Recreational Opportunities</span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="/Park-Hopper-Routes/images/parkimages/Charles_Young_Buffalo_Soldiers_National_Monument.jpg"
            alt="Charles Young Buffalo Soldiers National Monument"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Charles Young Buffalo National Monument</h3>
              <span className="card__badge">🗓️ Year round</span>
            </div>

            <p className="card__location">📍 Wilberforce, Ohio</p>

            <p className="card__description">
              Throughout his life, Charles Young overcame countless obstacles in
              his ascent to prominence. In spite of overt racism and stifling
              inequality, Young rose through the military ranks to become one of
              the most respected leaders of his time. A well-rounded man with a
              steadfast devotion to duty, Young led by example and inspired a
              generation of new leaders.
            </p>

            <div className="card__highlights">
              <span className="highlight">Historic Significance</span>
              <span className="highlight">Preserved Buffalo Herd</span>
              <span className="highlight">Historic Farm Complex</span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="/Park-Hopper-Routes/images/parkimages/Fire_Island_National_Seashore.jpg"
            alt="Fire Island National Seashore"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Fire Island National Seashore</h3>
              <span className="card__badge">🗓️ June - September</span>
            </div>

            <p className="card__location">📍 Ocean Beach, New York</p>

            <p className="card__description">
              Immerse yourself in an enchanting collage of coastal life and
              history. Rhythmic waves, high dunes, ancient maritime forests,
              historic landmarks and glimpses of wildlife, Fire Island has been
              a special place for diverse plants, animals and people for
              centuries. Far from the pressure of nearby big-city life, dynamic
              barrier island beaches offer solitude, camaraderie, and spiritual
              renewal.
            </p>

            <div className="card__highlights">
              <span className="highlight">Beaches and Oceanfront
              </span>
              <span className="highlight">Sunken Forest
              </span>
              <span className="highlight">Fire Island Lighthouse</span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="/Park-Hopper-Routes/images/parkimages/Everglades_National_Park.jpg"
            alt="Everglades National Park"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Theodore Roosevelt National Park</h3>
              <span className="card__badge">🗓️ May - September</span>
            </div>

            <p className="card__location">📍 Medora, North Dakota</p>

            <p className="card__description">
              When Theodore Roosevelt came to Dakota Territory to hunt bison in
              1883, he was a skinny, young, spectacled dude from New York. He
              could not have imagined how his adventure in this remote and
              unfamiliar place would forever alter the course of the nation. The
              rugged landscape and strenuous life that Roosevelt experienced here 
              would help shape a conservation policy that we still benefit from today.
            </p>

            <div className="card__highlights">
              <span className="highlight">
                Badlands Landscape
              </span>
              <span className="highlight">
                Wildlife Viewing
              </span>
              <span className="highlight">
                Theodore Roosevelt's Legacy
              </span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="/Park-Hopper-Routes/images/parkimages/Big_Bend_National_Park.jpg"
            alt="Big Bend National Park"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Big Bend National Park</h3>
              <span className="card__badge">🗓️ June - August</span>
            </div>

            <p className="card__location">📍 Alpine, TX</p>

            <p className="card__description">
              "There is a place in Far West Texas where night skies are dark as coal 
              and rivers carve temple-like canyons in ancient limestone. Here, at the 
              end of the road, hundreds of bird species take refuge in a solitary 
              mountain range surrounded by weather-beaten desert. Tenacious cactus 
              bloom in sublime southwestern sun, and species diversity is the best 
              in the country. This magical place is Big Bend...
            </p>

            <div className="card__highlights">
              <span className="highlight">Diverse Landscapes</span>
              <span className="highlight">Chisos Mountains</span>
              <span className="highlight">Rio Grande River</span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="/Park-Hopper-Routes/images/parkimages/Mount_Rushmore_National_Memorial.jpg"
            alt="Mount Rushmore National Memorial"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Mount Rushmore National Memorial</h3>
              <span className="card__badge">🗓️ May, September - October</span>
            </div>

            <p className="card__location">📍 Keystone, South Dakota</p>

            <p className="card__description">
              Majestic figures of George Washington, Thomas Jefferson, Theodore
              Roosevelt and Abraham Lincoln, surrounded by the beauty of the
              Black Hills of South Dakota, tell the story of the birth, growth,
              development and preservation of this country. From the history of
              the first inhabitants to the diversity of America today, Mount
              Rushmore brings visitors face to face with the rich heritage we
              all share.
            </p>

            <div className="card__highlights">
              <span className="highlight">The Monument</span>
              <span className="highlight">Sculptor Gutzon Borglum</span>
              <span className="highlight">Presidential Trail</span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  );
}

export default Cards;
