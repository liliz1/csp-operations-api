from unittest.mock import patch
from app.services import weather_service

@patch("app.services.weather_service.open_meteo_client.get_current_weather")
def test_get_forecast(mock_get_current_weather):
    #Simular un valor de retorno con return_value.
    mock_get_current_weather.return_value = {
        "current": {
            "temperature_2m": 25,
            "wind_speed_10m": 10,
            "cloud_cover": 40,
        }
    }

    resultado = weather_service.get_forecast(37.44, -6.25)

    assert resultado.temperature == 25
    assert resultado.wind_speed == 10
    assert resultado.cloud_cover == 40
    
    #Verificar que una dependencia fue llamada correctamente
    mock_get_current_weather.assert_called_once_with(37.44, -6.25)