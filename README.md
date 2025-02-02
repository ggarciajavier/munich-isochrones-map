# Munich Isochrones Map

Interactive map showing walking and cycling times from Munich subway stations using OpenStreetMap and OpenRouteService API.

## Setup

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## Structure

```
├── config.py                   # API key for OpenRouteService
├── constants.py                # Script constants
├── create_isochrones_map.py    # Main script
├── helpers.py                  # Helper functions
└── maps/                       # Output directory
    └── isochrones_map.html
```

## Usage

1. Set your OpenRouteService API key in `constants.py`.
2. Run the generator: `python create_isochrones_map.py`.

The script will:

- Fetch subway stations within the given box (e.g., 48.0613°N to 48.1892°N, 11.4663°E to 11.7293°E).
- Generate isochrones for:
  - 10 minute walking radius (blue)
  - 20 minute cycling radius (red)
- Create interactive map at `isochrones_map.html`isochrones_map.html