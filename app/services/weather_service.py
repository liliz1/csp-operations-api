from app.schemas.forecast import ForecastResponse
from app.clients import open_meteo_client


def get_forecast(latitude:float, longitude:float):     
    datos_json =open_meteo_client.get_current_weather(latitude,longitude)

    datos_devolver=ForecastResponse(
    temperature= datos_json["current"]["temperature_2m"],
    wind_speed= datos_json["current"]["wind_speed_10m"],
    cloud_cover= datos_json["current"]["cloud_cover"],
    )
    
    return datos_devolver

