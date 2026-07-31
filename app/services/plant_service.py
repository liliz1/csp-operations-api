from sqlalchemy.orm import Session
from app.models.plant import Plant
from app.schemas.plant import PlantCreate, PlantUpdate

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

def get_all_plants(session: Session):
    return session.query(Plant).all()


def get_plant_by_id(session:Session, plant_id:int):
    plant= session.query(Plant).filter(Plant.id==plant_id).first()
    if plant is None:
        return None
    return plant
#consulta la tabla plants, quédate solo con la fila cuyo id sea igual al que me han pasado, devuelve el primer resultado o None si no hay ninguno.

def update_plant(session:Session, plant_id:int, plant_data: PlantUpdate):
    plant= session.query(Plant).filter(Plant.id==plant_id).first()
    if plant is None:
        return None
    plant.name= plant_data.name
    plant.installed_power_mw= plant_data.installed_power_mw
    session.commit()
    session.refresh(plant)
    return plant

def delete_plant(session:Session, plant_id:int):
    plant = session.query(Plant).filter(Plant.id==plant_id).first()
    if plant is None:
        return None
    session.delete(plant)
    session.commit()

    return plant
    
