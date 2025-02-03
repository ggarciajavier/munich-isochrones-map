import requests

def transform_data(input_data) -> dict:
    """
    Transforms the OpenStreetMap JSON response into a dictionary format where each station
    is indexed by its ID. Each station entry contains key information like type, name,
    transport details and geographic coordinates.

    :param list input_data: A list of dictionaries containing station information from OpenStreetMap data
    :return: A dictionary where keys are station IDs and values are dictionaries containing station attributes
    """
    output_dict = {item['id']: {'type': item['type'],
                                'name': item['tags'].get('name'),
                                'public_transport': item['tags'].get('public_transport'),
                                'railway': item['tags'].get('railway'),
                                'station': item['tags'].get('station'),
                                'location': [item['lat'], item['lon']]
                                } 
                    for item in input_data}
    
    return output_dict


def obtain_subway_data(bbox) -> dict:
    """
    Queries OpenStreetMap's Overpass API for subway stations within the given
    geographical bounding box. Specifically looks for nodes tagged with
    railway=station and station=subway.

    :param list bbox: Map bounding box coordinates [south, west, north, east]
    :return: A dictionary where keys are station IDs and values are dictionaries containing station attributes
    """
    # Query OSM API to obtain all subway stations in a given box
    url = f'https://overpass-api.de/api/interpreter?' \
          f'data=[out:json];' \
          f'(node["railway"="station"]["station"="subway"]({",".join([str(x) for x in bbox])}););out;' \
          f'>;' \
          f'out skel qt;'
    r = requests.get(url).json()
    # Transform the response into a dictionary with station IDs as keys
    subway_data = transform_data(r['elements'])

    return subway_data


def obtain_isochrones(location, _params, _ors):
    """
    """
    # Reverse location
    rev_location = [list(reversed(location))]
    # Add location to params
    _params['locations'] = rev_location

    return _ors.isochrones(**_params)
