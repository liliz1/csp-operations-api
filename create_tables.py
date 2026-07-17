from app.core.database import Base, engine
# Importamos los modelos para que SQLAlchemy los registre
from app.models.plant import Plant

def main():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente.")


if __name__ == "__main__":
    main()


