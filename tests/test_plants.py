from fastapi.testclient import TestClient
from app.main import app

#Con TestClient no hace falta arrancar Uvicorn.
#El propio test llama directamente a tu aplicación FastAPI.
client = TestClient(app)

def test_get_plants():
    response = client.get("/plants")
    # comprueba que  el endpoint responde correctamente (200).
    assert response.status_code == 200
    # comprueba que el formato de la respuesta es el esperado (una lista).
    assert isinstance(response.json(),list)

def test_create_plant():
    response = client.post(
        "/plants",
        json={
            "name": "PS10",
            "latitude": 37.44,
            "longitude": -6.25,
            "installed_power_mw": 11.0,
        },
    )
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "PS10"
    assert data["installed_power_mw"]== 11.0
    assert data["id"]  is not None


def test_create_plant_error():
    response = client.post(
            "/plants",
            json={
        "name": "PS10",
        "latitude": 37.44,
        "longitude": -6.25,
        "installed_power_mw": -10
        },
    )
    data = response.json()
    assert data["detail"][0]["loc"][-1] == "installed_power_mw"
    assert response.status_code == 422

    