from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SupplierBase(BaseModel):
    name: str
    contact: Optional[str] = None
    email: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True

class IngredientBase(BaseModel):
    name: str
    quantity: float
    unit: str
    min_stock: Optional[float] = None
    supplier_id: int

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True

class StockMovementBase(BaseModel):
    ingredient_id: int
    movement_type: str
    quantity: float

class StockMovementCreate(StockMovementBase):
    pass

class StockMovement(StockMovementBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True