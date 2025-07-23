# 🗺️ Park Hopper Routes

A collaborative project between TripleTen Data Science and Software Engineering students focused on developing an online tool to plan a vacation to United States National Parks based on their starting location. The interactive experience also includes featured parks and helpful travel tips.

## 🌐 Live Demo

https://paul-london.github.io/Park-Hopper-Routes/

## 🚀 Project Overview

The goal of this project is to build a lightweight, functional tool that:

- Plans a vacation through a selection of National Parks based on the user's starting location
- Applies a route optimization algorithm to minimize travel distance (Greedy Nearest Neighbor)
- Displays the determined travel route on an interactive map
- Provide additional park information and travel tips

The framework of this project could serve additional use cases in delivery services, travel planning, field technician routing, or logistics.

## 📦 Features

- Clean and modular backend structure
- Basic frontend interface or API endpoint
- Input support: manual entry or uploaded data (e.g., CSV, JSON)
- Route optimization algorithm (TBD)
- Performance benchmarks and testing

## 🧠 Technologies

- Programming Language: `Python` / `JavaScript` / `REACT`
- Algorithm: Greedy Nearest Neighbor

## 🧑‍🤝‍🧑 Team Members

| Name    | Role                 |
| ------- | -------------------- |
| Lily Thato Anderson   | Software Engineering |
| Matthew Richards | Software Engineering |
| Vanessa Kwiatkoski | Software Engineering |
| Paul London   | Data Science         |
| Priti Sagar  | Data Science         |

## 📁 Project Structure (Tentative)

```text
Park-Hopper-Routes/
├── public/                      # Public static assets
│   └── vite.svg
├── scripts/                     # Python scripts (e.g., for map generation)
│   └── generate_map.py
├── src/                         # Main React app source
│   ├── assets/                  # Local image assets
│   │   ├── github.png
│   │   └── parkimages/
│   │       └── *.jpg
│   ├── components/              # Shared reusable components
│   │   ├── Footer.jsx
│   │   ├── Header.jsx
│   │   ├── Hero.jsx
│   │   ├── Itinerary.jsx
│   │   ├── MapDisplay.jsx
│   │   └── ParkCard.jsx
│   ├── contexts/                # Static data context (parksData.js)
│   ├── pages/                   # Top-level page components
│   │   └── Home.jsx
│   ├── App.jsx
│   └── main.jsx
├── maps/                        # Generated HTML maps from Python
│   └── *.html
├── docs/                        # GitHub Pages deployment output (via `npm run deploy`)
│   ├── assets/                  # Vite-generated assets
│   ├── images/                  # Copied images (referenced by relative paths)
│   │   └── parkimages/
│   └── *.html                   # Embedded map pages
├── .gitignore
├── index.html                   # Main HTML template
├── package.json
├── README.md
└── vite.config.js               # Vite configuration with GitHub Pages base path
```

## 🗓️ Timeline

| Phase          | Milestone                | Target Date |
| -------------- | ------------------------ | ----------- |
| 📌 Planning    | Define scope & algorithm | 7/17/2025   |
| 🔧 Development | Build core features      | 7/20/2025   |
| 🧪 Testing     | Deployment, Submission   | 7/22/2025   |
| 🚀 Launch      | Presentation             | 7/23/2025   |

## 📝 Notes

- Algorithm selection and trade-offs will be discussed as a group.
- Aim to build something that _works_, then iterate and optimize.
- Keep code modular and readable for team collaboration.

## 📬 Contact & Communication

Project coordination through [GitHub Issues](https://github.com/) and Discord.

---
