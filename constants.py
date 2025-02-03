# Bounding box for OpenStreetMaps. The order is: south, west, north, east.
BOUNDING_BOX = [48.0613, 11.4663, 48.1892, 11.7293]
# Parameters for walking isochrones
PARAMS_WALKING = {'profile': 'foot-walking',
                  'range': [600],  # 10 minutes walking
                  'smoothing': 10
                  }
# Parameters for cycling isochrones
PARAMS_CYCLING = {'profile': 'cycling-road',
                  'range': [1200],  # 20 minutes biking
                  'smoothing': 10
                  }
ORIGIN_STATION = 'Hauptbahnhof'
# Parameters for plotting
COLORS = {'walk': '#3399ff',
          'bike': '#cc3333'
          }
OUTPUT_FILE = './maps/isochrones_map.html'