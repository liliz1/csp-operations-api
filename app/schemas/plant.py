from pydantic import BaseModel

class PlantCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    installed_power_mw: float

class PlantUpdate(BaseModel):
    name: str
    installed_power_mw: float