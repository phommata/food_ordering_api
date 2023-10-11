from fastapi import APIRouter, Depends, HTTPException
from models.order import OrderReceipt, OrderRequest, OrderResponse
from menu import MenuService
import uuid

# Create an APIRouter
order_router = APIRouter()

class OrderItem:
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self, id, status, total, items):
        self.id = id
        self.status = status
        self.total = total
        self.items = [OrderItem(**item_data) for item_data in items]


class OrderService:
    def __init__(self, menu_service: MenuService):
        self.menu_service = menu_service
        
        # Mock data for order
        order_data = {
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
        self.orders = {order_id: Order(**order_data) for order_id, order_data in order_data.items()}

    # Function to create an order
    def create_order(self, order: OrderRequest):
        calculated_total = 0
        ordered_items = []

        for item in order.items:
            menu_item_found = None
            for menu_item in self.menu_service.get_menu_items():
                if item.id == menu_item.id:
                    menu_item_found = menu_item

            if not menu_item_found:
                raise HTTPException(status_code=400, detail="Invalid id")

            total_price = menu_item_found.price * item.quantity
            calculated_total += total_price

            # Create an OrderItem instance directly from the 'item' variable
            ordered_items.append(OrderItem(id=item.id, price=menu_item_found.price, quantity=item.quantity))

        id = str(uuid.uuid4())

        new_order = {
            "order_id": id,
            "status": "IN-PROGRESS",
            "total": calculated_total,
        }

        self.orders[id] = {
            "id": id,
            "status": "IN-PROGRESS",
            "total": calculated_total,
            "items": ordered_items
        }

        return new_order

    # Function to get an order receipt
    def get_order_receipt(self, order_id: str):
        order = self.orders.get(order_id)
        
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")

        return {
            "id": order.id,
            "status": order.status,
            "total": order.total,
            "items": [order_item.__dict__ for order_item in order.items]
        }
        
menu_service = MenuService()

order_service = OrderService(menu_service)

@order_router.post("/", response_model=OrderResponse)
async def create_order(order: OrderRequest, order_service: OrderService = Depends(lambda: order_service)):
    return order_service.create_order(order)

@order_router.get("/{order_id}", response_model=OrderReceipt)
async def get_order_receipt(order_id: str, order_service: OrderService = Depends(lambda: order_service)):
    return order_service.get_order_receipt(order_id)