from app.core.session import SessionLocal
from app.models.plant import Plant

def main():

    # Engine administra un pool de conexiones.
    session = SessionLocal() #la sesión obtiene una conexión del pool.

    try:
        plant = Plant(
            name="Gemasolar",
            latitude=37.56,
            longitude=-5.32,
            installed_power_mw=19.9,
        )

        session.add(plant) # SQLAlchemy marca ese objeto como pendiente de insertar.

        session.commit() # SQLAlchemy genera el SQL y lo envía a la base de datos.

        print("Planta insertada correctamente.")

    finally:
        session.close() # devuelve esa conexión al pool para que pueda reutilizarse.

if __name__ == "__main__" :
    main()