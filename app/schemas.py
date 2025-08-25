from pydantic import BaseModel

class StoreBase(BaseModel):
    name: str

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    id: int
    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    name: str
    store_id: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    name: str
    store_id: int

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    class Config:
        orm_mode = True

class SupplierBase(BaseModel):
    name: str
    store_id: int

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int
    class Config:
        orm_mode = True

class PurchaseBase(BaseModel):
    description: str
    amount: float
    store_id: int

class PurchaseCreate(PurchaseBase):
    pass

class Purchase(PurchaseBase):
    id: int
    class Config:
        orm_mode = True

class InvoiceBase(BaseModel):
    total: float
    customer_id: int
    store_id: int

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int
    class Config:
        orm_mode = True
