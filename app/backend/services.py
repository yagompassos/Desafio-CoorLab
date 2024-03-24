from typing import List

def get_best_transport_options(city_name: str, data: list):
    # Filtering transport data only to the selected city
    transport_list = [item for item in data if item['city'] == city_name]
    
    if not transport_list:
        return {}
    
    # Initialize best options with the first item in the list 
    fastest_transport = transport_list[0]
    cheapest_transport = transport_list[0]
    
    # Iterar sobre as outras opções de transporte para encontrar as melhores
    for transport_data in transport_list[1:]:
        # Converter a duração para horas
        duration_current = int(transport_data['duration'].replace('h', ''))
        fastest_duration = int(fastest_transport['duration'].replace('h', ''))
        
         # Check if it`s the fastest option untill now
        if duration_current < fastest_duration:
            fastest_transport = transport_data
        
        # Check if it`s cheapest option untill now
        if float(transport_data['price_econ'][3:]) < float(cheapest_transport['price_econ'][3:]):
            cheapest_transport = transport_data
    
    return {'fastest': fastest_transport, 'cheapest': cheapest_transport}
