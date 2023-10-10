from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_menu():
    response = client.get("/menu")
    assert response.status_code == 200
    menu_items = response.json()
    assert len(menu_items['items']) == 3 
    
    # verify the response
    assert menu_items == {
    "items": 
    [
        {
            "id": "781d66c4-87aa-469f-88df-1117c77fb576",
            "name": "Brooklyn Spaghetti",
            "genre": "ITALIAN",
            "price": 14.99
        },
        {
            "id": "b9024fb1-c3d9-4c5f-b447-0826e86988b4",
            "name": "Lamb Gyro",
            "genre": "GREEK",
            "price": 12.99
        },
        {
            "id": "f4f81a55-8f3d-4ae1-ae80-c81f51c0c49c",
            "name": "Cheeseburger",
            "genre": "AMERICAN",
            "price": 9.99
        }
    ]
}
