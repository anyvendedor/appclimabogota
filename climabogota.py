import requests

# API key para acceder a la API de OpenWeatherMap
api_key = "f2f4bce90638eed195dde9158b498059"

# URL de la API
url = f"http://api.openweathermap.org/data/2.5/weather?q=Bogota,CO&units=metric&appid={api_key}"

# Hacer una solicitud a la API
response = requests.get(url)

# Verificar que la respuesta sea exitosa
if response.status_code == 200:
    # Cargar la respuesta en formato JSON
    data = response.json()
    
    # Mostrar la temperatura actual en grados Celsius
    temperature = data["main"]["temp"]
    print(f"La temperatura actual en Bogotá es de {temperature} °C")
else:
    print("Error al obtener el clima")
