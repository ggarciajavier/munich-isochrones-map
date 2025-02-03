# 🗺️ Munich Isochrones Map

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/)
[![OpenRouteService](https://img.shields.io/badge/API-OpenRouteService-green.svg)](https://openrouteservice.org/)

## 🎯 Project Overview

A personal project to optimize apartment hunting in Munich using geospatial analysis. The tool uses OpenRouteService isochrones to identify areas that meet specific location criteria, e.g.:

- **🚶‍♂️ Walking**: Within 10 minutes of a subway station
- **🚲 Cycling**: Within 20 minutes to Munich Hauptbahnhof

## 🛠️ Tech Stack

- **OpenRouteService API**: Isochrone calculations
- **OpenStreetMap**: Base map data
- **Folium**: Interactive map visualization
- **Python**: Data processing

## 📁 Structure

```bash
├── config.py           # API key for OpenRouteService (not included)
├── constants.py                # Script constants
├── create_isochrones_map.py    # Main script
├── helpers.py                  # Helper functions
└── maps/                       # Output directory for maps
    └── isochrones_map.html
```

## 🚀 Getting Started

### Prerequisites

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration
1. Get API key from [OpenRouteService](https://api.openrouteservice.org/)
2. Create `config.py`:

```python
API_KEY = 'your_api_key_here'
```

### Run
```bash
python create_isochrones_map.py
```

## 🗺️ Output
The script generates an interactive map showing:

- 🔵 10-minute walking radius (blue)
- 🔴 20-minute cycling radius (red)
- 🚇 Munich subway stations

![Munich Isochrones Map Preview](./maps/map_preview.png)

---
_Built with ❤️ in Munich_