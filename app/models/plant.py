from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


#Cuando heredas de Base, SQLAlchemy empieza a inspeccionar la clase
#SQLAlchemy entiende que cada instancia de Plant representará una fila de la tabla.
class Plant(Base):
    __tablename__ = "plants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    latitude: Mapped[float]
    longitude:Mapped[float]
    installed_power_mw: Mapped[float]

