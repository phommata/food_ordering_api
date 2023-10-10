from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_order():
    order_data = {
        "items": [
            {
                "id": "781d66c4-87aa-469f-88df-1117c77fb576",
                "quantity": 1
            },
            {
                "id": "b9024fb1-c3d9-4c5f-b447-0826e86988b4",
                "quantity": 2
            },
            {
                "id": "f4f81a55-8f3d-4ae1-ae80-c81f51c0c49c",
                "quantity": 3
            },
        ]
    }
    response = client.post("/order", json=order_data)
    assert response.status_code == 200
    order = response.json()
    
    # verify the response
    assert order['status'] == "IN-PROGRESS"
    assert order['total'] == 70.94

def test_get_order_receipt():
    response_get_receipt = client.get(f"/order/c424989e-6760-45bd-bacd-dad9a4e9efd6")
    assert response_get_receipt.status_code == 200
    receipt = response_get_receipt.json()
 
    # verify the response
    assert receipt == {
    "id": "c424989e-6760-45bd-bacd-dad9a4e9efd6",
    "status": "COMPLETE",
    "total": 70.94,
    "items": [
        {
            "id": "781d66c4-87aa-469f-88df-1117c77fb576",
            "price": 14.99,
            "quantity": 1
        },
        {
            "id": "b9024fb1-c3d9-4c5f-b447-0826e86988b4",
            "price": 12.99,
            "quantity": 2
        },
        {
            "id": "f4f81a55-8f3d-4ae1-ae80-c81f51c0c49c",
            "price": 9.99,
            "quantity": 3
        }
    ]
}