from pydantic import BaseModel
from typing import List

class OrderItemBase(BaseModel):
    id: str
    quantity: int

class OrderItem(OrderItemBase):
    price: float

class OrderRequest(BaseModel):
    items: List[OrderItemBase]
    
class OrderResponse(BaseModel):
    order_id: str
    status: str
    total: float

class OrderReceipt(BaseModel):
    id: str
    status: str
    total: float
    items: List[OrderItem]
