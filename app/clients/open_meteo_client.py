import httpx

def get_current_weather():
    url="https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": 37.39,
        "longitude": -5.99,
        #"hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
	    "current": ["temperature_2m", "wind_speed_10m" ,  "cloud_cover"],
        #"current2": "temperature_2m,wind_speed_10m,cloud_cover"
    }

    response= httpx.get(url, params=params, timeout=10)
    response.raise_for_status()
    
    # try:
    #     response= httpx.get(url, params=params, timeout=10)
    #     response.raise_for_status()
    # except httpx.HTTPError as e:
    #     raise RuntimeError("No se pudo obtener la predicción") from e
    
    return response.json()