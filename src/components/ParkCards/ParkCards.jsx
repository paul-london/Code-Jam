import "./ParkCards.css";

function Cards() {
  return (
    <div className="cards">
      <ul className="cards__container">
        <li className="card">
          <img
            src="/Park-Hopper-Routes/images/parkimages/Golden-gate.jpg"
            alt="Golden Gate"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Golden Gate National</h3>
              <span className="card__badge">🗓️ May - October</span>
            </div>

            <p className="card__location">📍 San Franciso, Califonia</p>

            <p className="card__description">
              Experience a park so rich it supports 19 distinct ecosystems with
              over 2,000 plant and animal species. Go for a hike, enjoy a vista,
              have a picnic or learn about the centuries of overlapping history
              from California\u2019s indigenous cultures, Spanish colonialism,
              the Mexican Republic, US military expansion and the growth of San
              Francisco. All of this and more awaits you, so get out and find
              your park.
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
            src="/Park-Hopper-Routes/images/parkimages/Charles-young-park.jpg"
            alt="Charles Young National"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Charles Young Buffalo National</h3>
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
              <span className="highlight">Youngsholm</span>
              <span className="highlight">Buffalo Soldiers Legacy</span>
              <span className="highlight">Guided Tours & Ranger Programs</span>
            </div>
          </div>
        </li>

        <li className="card">
          <img
            src="/Park-Hopper-Routes/images/parkimages/Fire-island-national.jpg"
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
            src="/Park-Hopper-Routes/images/parkimages/Theodore-national-park.jpg"
            alt="Theodore Roosevelt National Park"
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
              rugged landscape and strenuous life that TR experienced here would
              help shape a conservation policy that we still benefit from today.
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
            src="/Park-Hopper-Routes/images/parkimages/Kenilwork-park.jpg"
            alt="Kenilworth Park & Aquatic Gardens"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Kenilworth Park & Aquatic Gardens</h3>
              <span className="card__badge">🗓️ June - August</span>
            </div>

            <p className="card__location">📍 Washionton,DC</p>

            <p className="card__description">
              Deep within Kenilworth lies an oasis, hidden behind trees and
              cattails. It's a place where beavers build their homes and turtles
              sleep on logs. Lotus blooms rise from the muck and lilies sit on
              the water. The wind dances with the dragonflies, rustling through
              the trees, carrying the song of the birds until it brushes across
              your face, fading to a whisper, saying \"come join.\"
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
            src="/Park-Hopper-Routes/images/parkimages/Mount-rushmore-park.jpg"
            alt="Mount Rushmore National Memorial"
            className="card__image"
          />

          <div className="card__content">
            <div className="card__heading">
              <h3 className="card__title">Mount Rushmore National </h3>
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
              <span className="highlight">Cataract Falls</span>
              <span className="highlight">Cades Cove</span>
              <span className="highlight">Appalachian Trail</span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  );
}

export default Cards;
