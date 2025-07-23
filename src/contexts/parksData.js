const parks = [
  {
    id: "0E797FA8-6E31-418B-A68F-13CEE37A2AF5",
    name: "Golden Gate National Recreation Area",
    location: "California",
    latitude: 37.85982543,
    longitude: -122.6007386,
    description:
      "Experience a park so rich it supports 19 distinct ecosystems with over 2,000 plant and animal species. Go for a hike, enjoy a vista, have a picnic or learn about the centuries of overlapping history from California\u2019s indigenous cultures, Spanish colonialism, the Mexican Republic, US military expansion and the growth of San Francisco. All of this and more awaits you, so get out and find your park.",
    url: "https://www.nps.gov/goga/index.htm",
    image_url:
      "https://www.nps.gov/common/uploads/structured_data/3C7FEE17-1DD8-B71B-0BA285725552D8E3.jpg",
  },
  {
    id: "FB1AE18D-522F-434B-9983-3D0194CE1995",
    name: "Fort Union National Monument",
    location: "New Mexico",
    latitude: 35.90700629,
    longitude: -105.0145185,
    description:
      "Exposed to the wind, within a sweeping valley of short grass prairie, and along the eroded Santa Fe Trail, lie the adobe walled ruins of the largest 19th century military fort in the region. From 1851 to 1891, Fort Union functioned as an agent of change, desired or not, in the New Mexico Territory and throughout the Southwest.",
    url: "https://www.nps.gov/foun/index.htm",
    image_url:
      "https://www.nps.gov/common/uploads/structured_data/3C7C1B33-1DD8-B71B-0B88C189AAA85B01.jpg",
  },
  {
    id: "5590468F-2446-4B46-A8C1-42505177C298",
    name: "Mount Rushmore National Memorial",
    location: "South Dakota",
    latitude: 43.88037021,
    longitude: -103.4525186,
    description:
      "Majestic figures of George Washington, Thomas Jefferson, Theodore Roosevelt and Abraham Lincoln, surrounded by the beauty of the Black Hills of South Dakota, tell the story of the birth, growth, development and preservation of this country. From the history of the first inhabitants to the diversity of America today, Mount Rushmore brings visitors face to face with the rich heritage we all share.",
    url: "https://www.nps.gov/moru/index.htm",
    image_url:
      "https://www.nps.gov/common/uploads/structured_data/B8BC21F3-9292-822E-797779C6FA2B9497.jpg",
  },
  {
    name: "Theodore Roosevelt National Park",
    location: "North Dakota",
    latitude: 47.17777274,
    longitude: -103.4300083,
    description:
      "When Theodore Roosevelt came to Dakota Territory to hunt bison in 1883, he was a skinny, young, spectacled dude from New York. He could not have imagined how his adventure in this remote and unfamiliar place would forever alter the course of the nation. The rugged landscape and strenuous life that TR experienced here would help shape a conservation policy that we still benefit from today.",
    url: "https://www.nps.gov/thro/index.htm",
    image_url:
      "https://www.nps.gov/common/uploads/structured_data/3C793AD5-1DD8-B71B-0B4A3C1BFA5B4C83.jpg",
  },
  {
    id: "22177869-21C7-49A1-961C-3F2114F01007",
    name: "Charles Young Buffalo Soldiers National Monument",
    location: "Ohio",
    latitude: 39.70817829,
    longitude: -83.89328575,
    description:
      "Throughout his life, Charles Young overcame countless obstacles in his ascent to prominence. In spite of overt racism and stifling inequality, Young rose through the military ranks to become one of the most respected leaders of his time. A well-rounded man with a steadfast devotion to duty, Young led by example and inspired a generation of new leaders.",
    url: "https://www.nps.gov/chyo/index.htm",
    image_url:
      "https://www.nps.gov/common/uploads/structured_data/0645BF55-CF33-994E-F247098090A7E65C.jpg",
  },
  {
    id: "A1901BAE-94DB-44E4-96D4-1E07422EDF6E",
    name: "Kenilworth Park & Aquatic Gardens",
    location: "Washington, DC",
    latitude: 38.9128,
    longitude: -76.9434,
    description:
      'Deep within Kenilworth lies an oasis, hidden behind trees and cattails. It\'s a place where beavers build their homes and turtles sleep on logs. Lotus blooms rise from the muck and lilies sit on the water. The wind dances with the dragonflies, rustling through the trees, carrying the song of the birds until it brushes across your face, fading to a whisper, saying "come join."',
    url: "https://www.nps.gov/keaq/index.htm",
    image_url:
      "https://www.nps.gov/common/uploads/structured_data/3C819F7C-1DD8-B71B-0BE9077BC0E39492.jpg",
  },
  {
    id: "E6E1D22A-7A89-47F8-813C-B611059A8CF9",
    name: "African Burial Ground National Monument",
    location: "New York",
    latitude: 40.71452681,
    longitude: -74.00447358,
    description:
      "The African Burial Ground is the oldest and largest known excavated burial ground in North America for both free and enslaved Africans. It serves to protect and honor the historic role that slavery played in shaping New York's development.",
    url: "https://www.nps.gov/afbg/index.htm",
    image_url:
      "https://www.nps.gov/common/uploads/structured_data/3C8554EA-1DD8-B71B-0BE6FF3BF04C18B8.jpg",
  },
  {
    id: "C200ADA5-F162-4D77-A820-950E13925129",
    name: "Vanderbilt Mansion National Historic Site",
    location: "New York",
    latitude: 41.79697937,
    longitude: -73.94205557,
    description:
      "Built by of one of the first families of wealth in America. Designed by one of the nation's preeminent architects. The Vanderbilt Mansion is a home built expressly for the aristocratic lifestyle.",
    url: "https://www.nps.gov/vama/index.htm",
    image_url:
      "https://www.nps.gov/common/uploads/structured_data/3C810D33-1DD8-B71B-0B857963C3AEC92E.jpg",
  },
  {
    id: "8A31246D-5AB9-4A0E-8FBA-A9780C468935",
    name: "Fire Island National Seashore",
    location: "New York",
    latitude: 40.69668638,
    longitude: -73.00013462,
    description:
      "Immerse yourself in an enchanting collage of coastal life and history. Rhythmic waves, high dunes, ancient maritime forests, historic landmarks and glimpses of wildlife, Fire Island has been a special place for diverse plants, animals and people for centuries. Far from the pressure of nearby big-city life, dynamic barrier island beaches offer solitude, camaraderie, and spiritual renewal.",
    url: "https://www.nps.gov/fiis/index.htm",
    image_url:
      "https://www.nps.gov/common/uploads/structured_data/3C7D4BAC-1DD8-B71B-0B8798F96FC8F8D7.jpg",
  },
];

export default parks;
