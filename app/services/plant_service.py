from sqlalchemy.orm import Session
from app.models.plant import Plant
from app.schemas.plant import PlantCreate

def create_plant(session:Session, plant_data:PlantCreate) -> Plant:
    #   -> Plant: Declara que la salida final será un objeto de tipo Plant.
    plant = Plant(
        name=plant_data.name,
        latitude=plant_data.latitude,
        longitude=plant_data.longitude,
        installed_power_mw=plant_data.installed_power_mw,
    )

    session.add(plant)
    session.commit()
    session.refresh(plant)

    return plant

def get_plants(session: Session):
    return session.query(Plant).all()


def get_plant_by_id(session:Session, plant_id:int):
    return session.query(Plant).filter(Plant.id==plant_id).first()
#consulta la tabla plants, quédate solo con la fila cuyo id sea igual al que me han pasado, devuelve el primer resultado o None si no hay ninguno.