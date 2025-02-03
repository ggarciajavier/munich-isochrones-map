import time

import folium
from openrouteservice import client

import constants
from config import API_KEY
from helpers import obtain_subway_data, obtain_isochrones


def add_isochrones_to_map(data, constants) -> dict:
    """
    Include isochrones to the map_data dictionary.

    :param dict data: Dictionary with station IDs as keys and station attributes as values
    :param dict constants: Constant settings
    :return: The dictionary with the isochrones added
    """
    # Get the OpenRouteService client
    ors = client.Client(key=API_KEY)
    
    # Walking isochrones: it adds the isochrones to the station attributes
    stations = list(data.keys())
    for id in stations:
        # Get the station location
        location = data[id]['location']
        # Pause 3 sec to respect limit of 20 queries per minute
        time.sleep(3)
        # Get the isochrones
        isochrones = obtain_isochrones(location, constants.PARAMS_WALKING, ors)
        # Add the isochrones to the map data
        data[id]['isochrone_walk'] = isochrones
    
    # Biking isochrone: it is added to the map data as a separate entry
    origin_station = constants.ORIGIN_STATION
    origin_id = [id for id, data in data.items() 
                  if origin_station.lower() in data['name'].lower()][0]
    origin_location = data[origin_id]['location']
    data['isochrone_bike'] = obtain_isochrones(origin_location,
                                               constants.PARAMS_CYCLING,
                                               ors
                                               )

    return data


def create_isochrones_map(map_data, constants):
    """
    Create a map with the isochrones and station locations.

    :param dict map_data: Dictionary with station IDs as keys and station attributes as values
    :param dict constants: Constant settings
    """
    # Initialize map
    bbox = constants.BOUNDING_BOX
    my_map = folium.Map(location=((bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2), 
                        zoom_start=11)
    # Define colors
    colors = constants.COLORS
    # Plot biking isocrhone
    folium.features.GeoJson(data=map_data['isochrone_bike'],
                            style_function=lambda feature: {'stroke': True,
                                                            'color': colors['bike'],
                                                            'weight': 1,
                                                            'fillOpacity': 0.3,
                                                            'fillColor': colors['bike']}
                            ).add_to(my_map)
    # Plot walking isochrones and stations
    stations = [id for id in map_data.keys() if type(id) == int]
    for id in stations:
        # Add walking isochrones
        folium.features.GeoJson(data=map_data[id]['isochrone_walk'],
                                style_function=lambda feature: {'stroke': False,
                                                                'fillOpacity': 0.3,
                                                                'fillColor': colors['walk']}
                                ).add_to(my_map)
        # Add station markers
        folium.CircleMarker(location=map_data[id]['location'], 
                            radius=1,
                            popup=map_data[id]['name']).add_to(my_map)
    # Add legend
    walk_time = int(constants.PARAMS_WALKING['range'][0] / 60)
    bike_time = int(constants.PARAMS_CYCLING['range'][0] / 60)
    legend_html = f'''
              <div style="
              position: fixed; 
              bottom: 50px; left: 110px; 
              width: 300px; height: 60px; 
              background-color: white; opacity: 0.75;
              z-index:9999; 
              font-size:14px;
              padding: 10px;
              text-align: left;
              display: flex;
              align-items: center;
              justify-content: center;
              ">
              <div style="margin-left: 5px;">
              <i class="fa fa-circle" style="color:{colors['walk']}"></i> {walk_time}-minute walk to a subway station<br>
              <i class="fa fa-circle" style="color:{colors['bike']}"></i> {bike_time}-minute bike ride to {constants.ORIGIN_STATION}
              </div>
              </div>
              '''
    my_map.get_root().html.add_child(folium.Element(legend_html))
    # Store map
    output_file = constants.OUTPUT_FILE
    print(f'Saving map to {output_file}')
    my_map.save(output_file)


def main():
    print('\n### Isochrones Map Started ###\n')
    start_time = time.time()
    # Get the subway station nodes from OpenStreetMap
    print(f'Retrieving subway station data from OpenStreetMap for {constants.BOUNDING_BOX}...')
    map_data = obtain_subway_data(constants.BOUNDING_BOX)
    # Get list of stations
    stations = list(map_data.keys())
    print(f'{len(stations)} subway stations found.')
    # Add isochrones to the map_data
    print('Obtaining isochrones. This might take a while...')
    map_data = add_isochrones_to_map(map_data, constants)
    print('Isochrones obtained.')
    # Create the map
    create_isochrones_map(map_data, constants)
    print('\n### Process ended ###\n')
    # Calculate and print the total elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Total elapsed time: {elapsed_time:.2f} seconds\n')


if __name__ == '__main__':
    main()