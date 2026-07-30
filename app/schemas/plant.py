from pydantic import BaseModel, Field

class PlantCreate(BaseModel):
    name: str=Field(min_length=1)
    latitude: float= Field(ge=-90,le=90)
    longitude: float= Field(ge=-180, le=180)
    installed_power_mw: float= Field(gt=0)

class PlantUpdate(BaseModel):
    name: str
    installed_power_mw: float