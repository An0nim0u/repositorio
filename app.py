import requests
import json
from datetime import datetime

# Función para obtener la ubicación del dispositivo
def get_location():
    try:
        # Obtener la ubicación del dispositivo
        location_data = requests.get('https://ipapi.co/json/').json()
        latitude = location_data['latitude']
        longitude = location_data['longitude']
        location = f'Latitud: {latitude}, Longitud: {longitude}'

        # Obtener la fecha y hora actual
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Enviar los datos al servidor local
        data = {
            'latitude': latitude,
            'longitude': longitude,
            'timestamp': timestamp
        }
        response = requests.post('http://localhost:5000/location', data=json.dumps(data), headers={'Content-Type': 'application/json'})
        print(f'Ubicación enviada al servidor: {response.text}')
    except Exception as e:
        print(f'Error al obtener la ubicación: {e}')

if __name__ == '__main__':
    get_location()
