import "./ParkCards.css";

function Cards() {
  return (
    <div className="cards">
      <ul className="cards__container">
        <li className="card">
          <img
            src="src\assets\goldenGate.webp"
            alt="Golden Gate National Recreation Area"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">
                Golden Gate National Recreation Area
              </h3>
              <span className="card__badge">
                🗓️ April - May, September - October
              </span>
            </div>

            <p className="card__location">📍 Tennessee, North Carolina</p>

            <p className="card__description">
              America's most visited national park, famous for its misty
              mountains, diverse wildlife, and Appalachian culture.
            </p>

            <div className="card__highlights">
              <span className="highlight">Cataract Falls</span>
              <span className="highlight">Cades Cove</span>
              <span className="highlight">Appalachian Trail</span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="src\assets\charlesYoungSolider.jpg"
            alt="Charles Young Buffalo Soldiers National Monument"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">
                Charles Young Buffalo Soldiers National Monument
              </h3>
              <span className="card__badge">
                🗓️ April - May, September - October
              </span>
            </div>

            <p className="card__location">📍 Wilberforce, Ohio</p>

            <p className="card__description">
              Charles Young Buffalo Soldiers National Monument honors the life
              and legacy of Colonel Charles Young, a pioneering African American
              Army officer and leader of the Buffalo Soldiers,
            </p>

            <div className="card__highlights">
              <span className="highlight">Youngsholm</span>
              <span className="highlight">Buffalo Soldiers Legacy</span>
              <span className="highlight">Guided Tours & Ranger Programs</span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="src\assets\fortPark.jpg"
            alt="Theodore Roosevelt National Park"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Theodore Roosevelt National Park</h3>
              <span className="card__badge">
                🗓️ April - May, September - October
              </span>
            </div>

            <p className="card__location">📍 Medora, North Dakota</p>

            <p className="card__description">
              Theodore Roosevelt National Park preserves the rugged Badlands of
              western North Dakota—where Theodore Roosevelt found solace,
              inspiration, and his conservation calling—in three distinct units
              near Medora
            </p>

            <div className="card__highlights">
              <span className="highlight">
                Maltese Cross Cabin & Elkhorn Ranch Site
              </span>
              <span className="highlight">
                Spectacular Badlands & Scenic Drives
              </span>
              <span className="highlight">Wildlife & Geologic Wonders</span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="src/assets/Mountain-clouds.jpg"
            alt="Fort Union National Monument"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Fort Union National Monument</h3>
              <span className="card__badge">
                🗓️ April - May, September - October
              </span>
            </div>

            <p className="card__location">📍Watrous, New Mexico</p>

            <p className="card__description">
              Fort Union National Monument preserves the ruins of three U.S.
              Army forts built from 1851 to 1891 near the junction of the Santa
              Fe Trail, showcasing the largest 19th-century military fort in the
              Southwest, now set amid sweeping prairie landscape.
            </p>

            <div className="card__highlights">
              <span className="highlight">
                Three Successive Fort Sites & Santa Fe Trail Ruts
              </span>
              <span className="highlight">
                Major Civil‑War‑Era Supply Depot
              </span>
              <span className="highlight">
                Guided & Self‑Guided Trails with Ranger Programs
              </span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="src\assets\fireisland.jpg"
            alt="Fire Island National Seashore"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Fire Island National Seashore</h3>
              <span className="card__badge">
                🗓️ April - May, September - October
              </span>
            </div>

            <p className="card__location">
              📍 Patchogue / Fire Island, New York
            </p>

            <p className="card__description">
              Fire Island National Seashore protects a 26-mile stretch of
              pristine barrier island off southern Long Island, preserving
              dynamic beaches, maritime forests, historic communities, and
              cultural landmarks near Patchogue and Babylon, New York.
            </p>

            <div className="card__highlights">
              <span className="highlight">Fire Island Lighthouse</span>
              <span className="highlight">
                Sunken Forest & Otis Pike Wilderness
              </span>
              <span className="highlight">
                Secluded Beaches & Vibrant Communities
              </span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="src\assets\rushmore.jpg"
            alt="Mount Rushmore National Memorial"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Mount Rushmore National Memorial</h3>
              <span className="card__badge">
                🗓️ April - May, September - October
              </span>
            </div>

            <p className="card__location">📍 Keystone, South Dakota</p>

            <p className="card__description">
              Mount Rushmore National Memorial is a monumental granite sculpture
              featuring the 60‑foot carved heads of Presidents George
              Washington, Thomas Jefferson, Theodore Roosevelt, and Abraham
              Lincoln—symbolizing the birth, growth, development, and
              preservation of the United States—set high in the forested Black
              Hills near Keystone.
            </p>

            <div className="card__highlights">
              <span className="highlight">
                Avenue of Flags & Grand View Terrace
              </span>
              <span className="highlight">
                Presidential Trail & Sculptor’s Studio
              </span>
              <span className="highlight">
                Evening Lighting Ceremony & Ranger Talks
              </span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  );
}

export default Cards;
