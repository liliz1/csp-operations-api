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


def test_get_plant_by_id():
    # Crear una planta (Arrange)

    create_response = client.post(
        "/plants",
        json={
            "name": "Plant_1",
            "latitude": 39.44,
            "longitude": -9.25,
            "installed_power_mw": 50.0,
        },
    )
    # comprobamos que se ha creado la planta correctamente
    assert create_response.status_code == 200
    # Obtener el id
    plant_id= create_response.json()["id"]
    # Hacer el GET (Act)
    response = client.get(f"/plants/{plant_id}")
    # Comprobar el resultado (Assert)
    assert response.status_code == 200
    # comprobamos que hemos recuperado la planta correcta
    data = response.json()
    assert data["id"] == plant_id
    assert data["name"] == "Plant_1"
    assert data["installed_power_mw"] == 50.0


def test_get_plant_by_id_not_found():
    response = client.get("/plants/999999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Plant Not Found"




def test_put_plant():
    # Arrange. Crear una planta
    create_response = client.post(
        "/plants",
        json={
            "name": "Plant_2",
            "latitude": 60.44,
            "longitude": -18.25,
            "installed_power_mw": 80.0,
        },
    )
    # comprobamos que se ha creado la planta correctamente
    assert create_response.status_code == 200
    # obtenemos el id
    plant_id = create_response.json()["id"]
    # Act. Hacer el PUT con los nuevos datos
    response = client.put(
        f"/plants/{plant_id}",
        json={
            "name": "Plant_2_Actualizada",
            "installed_power_mw": 75.0,
        }
    )
    # Assert. Comprobar la respuesta
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == plant_id
    assert data["name"] == "Plant_2_Actualizada"
    assert data["installed_power_mw"] ==  75.0
    # Comprobar que los campos que no se actualizan siguen con el mismo valor.
    assert data["latitude"] == 60.44
    assert data["longitude"] == -18.25


    def test_put_plant_not_found():
        response = client.put(
            "/plants/999999",
            json={
                "name": "Plant_actualizada",
                "installed_power_mw": 75.0,
            }
        )
        assert response.status_code == 404
        
        data = response.json()
        assert data["detail"] == "Plant Not Found"