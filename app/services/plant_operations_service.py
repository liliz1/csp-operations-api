from sqlalchemy.orm import Session
import app.services.plant_service as ps
import app.services.weather_service as ws


def get_forecast_for_plant(session: Session, plant_id: int):
    plant= ps.get_plant_by_id(session, plant_id)
    if plant is None:
        return None
    return ws.get_forecast(plant.latitude, plant.longitude)
     


    

