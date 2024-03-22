from typing import List
from .models import Transport

def get_best_transport_options(city_name: str) -> List[Transport]:
    # Filtre os dados de transporte para a cidade específica
    transport_list = [item for item in data if item['city'] == city_name]
    
    # Se não houver transporte disponível para a cidade, retorne uma lista vazia
    if not transport_list:
        return []
    
    # Inicialize as melhores opções de transporte como a primeira opção encontrada
    best_options = [Transport(**transport_list[0])]
    min_price_confort = float(transport_list[0]['price_confort'][3:])  # Remova o 'R$ ' e converta para float
    min_price_econ = float(transport_list[0]['price_econ'][3:])  # Remova o 'R$ ' e converta para float
    
    # Itere sobre as outras opções de transporte para encontrar as melhores
    for transport_data in transport_list[1:]:
        price_confort = float(transport_data['price_confort'][3:])  # Remova o 'R$ ' e converta para float
        price_econ = float(transport_data['price_econ'][3:])  # Remova o 'R$ ' e converta para float
        
        # Verifique se é a opção mais confortável até agora
        if price_confort < min_price_confort:
            best_options = [Transport(**transport_data)]
            min_price_confort = price_confort
        # Verifique se é a opção mais econômica até agora
        elif price_econ < min_price_econ:
            best_options = [Transport(**transport_data)]
            min_price_econ = price_econ
        # Se for igual ao preço mínimo, adicione à lista de melhores opções
        elif price_confort == min_price_confort and price_econ == min_price_econ:
            best_options.append(Transport(**transport_data))
    
    return best_options
