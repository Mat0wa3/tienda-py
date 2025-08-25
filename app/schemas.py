from pydantic import BaseModel
from typing import Optional

# --- STORE ---
class StoreBase(BaseModel):
    name: str

class StoreCreate(StoreBase):
    pass

class StoreUpdate(BaseModel):
    name: Optional[str]

class Store(StoreBase):
    id: int
    class Config:
        orm_mode = True


# --- EMPLOYEE ---
class EmployeeBase(BaseModel):
    name: str
    store_id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str]
    store_id: Optional[int]

class Employee(EmployeeBase):
    id: int
    class Config:
        orm_mode = True


# --- CUSTOMER ---
class CustomerBase(BaseModel):
    name: str
    store_id: int

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str]
    store_id: Optional[int]

class Customer(CustomerBase):
    id: int
    class Config:
        orm_mode = True


# --- SUPPLIER ---
class SupplierBase(BaseModel):
    name: str
    store_id: int

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    name: Optional[str]
    store_id: Optional[int]

class Supplier(SupplierBase):
    id: int
    class Config:
        orm_mode = True


# --- PURCHASE ---
class PurchaseBase(BaseModel):
    description: str
    amount: float
    store_id: int

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseUpdate(BaseModel):
    description: Optional[str]
    amount: Optional[float]
    store_id: Optional[int]

class Purchase(PurchaseBase):
    id: int
    class Config:
        orm_mode = True


# --- INVOICE ---
class InvoiceBase(BaseModel):
    total: float
    customer_id: int
    store_id: int

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(BaseModel):
    total: Optional[float]
    customer_id: Optional[int]
    store_id: Optional[int]

class Invoice(InvoiceBase):
    id: int
    class Config:
        orm_mode = True
