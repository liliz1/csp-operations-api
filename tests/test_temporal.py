from app.core.session import SessionLocal
from app.models.plant import Plant

def test_database_query():
    session = SessionLocal()

    try:
        print("Antes de la consulta")
        plants = session.query(Plant).all()
        print("Después de la consulta")
        print(plants)
    finally:
        session.close()