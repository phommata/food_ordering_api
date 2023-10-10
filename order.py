from fastapi import APIRouter, HTTPException
from models.order import OrderReceipt, OrderRequest, OrderResponse
from menu import menu_items
import uuid

# Create an APIRouter
order_router = APIRouter()

# Mock data for order
orders = {
    "c424989e-6760-45bd-bacd-dad9a4e9efd6" : {
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
}

# Function to create an order
@order_router.post("/", response_model=OrderResponse)
async def create_order(order: OrderRequest):
    calculated_total = 0
    ordered_items = []

    for item in order.items:
        for menu_item in menu_items["items"]:
            if item.id == menu_item["id"]:
                menu_item_found = menu_item
        
        if not menu_item_found:
            raise HTTPException(status_code=400, detail="Invalid id")

        total_price = menu_item_found["price"] * item.quantity
        calculated_total += total_price

        ordered_items.append({
            "id": menu_item_found["id"],
            "price": menu_item_found["price"],
            "quantity": item.quantity,
        })

    id = str(uuid.uuid4())

    new_order = {
        "order_id": id,
        "status": "IN-PROGRESS",
        "total": calculated_total,
    }
    
    orders[id] = {
        "id": id,
        "status": "IN-PROGRESS",
        "total": calculated_total,
        "items": ordered_items
    }

    return new_order

# Function to get an order receipt
@order_router.get("/{id}", response_model=OrderReceipt)
async def get_order_receipt(id: str):
    order = orders[id] if id in orders else None
    
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    return {
        "id": order["id"],
        "status": order["status"],
        "total": order["total"],
        "items": order["items"]
    }
