from fastapi import FastAPI, HTTPException, Depends
from app.services import weather_service
from app.schemas.forecast import ForecastResponse
from sqlalchemy.orm import Session
from app.core.session import SessionLocal
from app.schemas.plant import PlantCreate
from app.services import plant_service
from app.core.dependencies import get_session

app = FastAPI()

Latitud= 37.39
Longitud=-5.99

@app.get("/health")
def health():
    return {
    "status": "ok"
}

# con response_model, FastAPI validará automáticamente la respuesta(debe cumplir el contrato ForecastResponse) antes de enviarla
@app.get("/forecast", response_model=ForecastResponse)
def forecast():
    try:
        return weather_service.get_forecast()
    except RuntimeError:
        raise HTTPException(
            status_code=503,
            detail= "Servicio meteorológico no disponible"
        )

@app.post("/plants")
def create_plant(plant: PlantCreate, session: Session = Depends(get_session)):
                                # Necesita una Session y le dice a FastAPI que la consiga

    return plant_service.create_plant(session, plant)

@app.get("/plants")
def get_plants(session: Session=Depends(get_session)):
    return plant_service.get_plants(session)

@app.get("/plants/{plant_id}")
def get_plant_by_id (plant_id: int, session:Session=Depends(get_session)):
    plant= plant_service.get_plant_by_id(session, plant_id)

    if plant is None:
        raise HTTPException(
            status_code=404,
            detail= "Plant Not Found"
        ) 

    return plant

