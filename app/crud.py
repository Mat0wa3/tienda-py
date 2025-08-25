from sqlalchemy.orm import Session
from app import models, schemas

def create_store(db: Session, store: schemas.StoreCreate):
    db_store = models.Store(name=store.name)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

def get_stores(db: Session):
    return db.query(models.Store).all()

def update_store(db: Session, store_id: int, store_update: schemas.StoreUpdate):
    db_store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if not db_store:
        return None
    for key, value in store_update.dict(exclude_unset=True).items():
        setattr(db_store, key, value)
    db.commit()
    db.refresh(db_store)
    return db_store

def delete_store(db: Session, store_id: int):
    db_store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if not db_store:
        return None
    db.delete(db_store)
    db.commit()
    return db_store

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session):
    return db.query(models.Employee).all()

def update_employee(db: Session, employee_id: int, employee_update: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not db_employee:
        return None
    for key, value in employee_update.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not db_employee:
        return None
    db.delete(db_employee)
    db.commit()
    return db_employee

# Customers
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customers(db: Session):
    return db.query(models.Customer).all()

def update_customer(db: Session, customer_id: int, customer_update: schemas.CustomerUpdate):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        return None
    for key, value in customer_update.dict(exclude_unset=True).items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        return None
    db.delete(db_customer)
    db.commit()
    return db_customer

# Suppliers
def create_supplier(db: Session, supplier: schemas.SupplierCreate):
    db_supplier = models.Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def get_suppliers(db: Session):
    return db.query(models.Supplier).all()

def update_supplier(db: Session, supplier_id: int, supplier_update: schemas.SupplierUpdate):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not db_supplier:
        return None
    for key, value in supplier_update.dict(exclude_unset=True).items():
        setattr(db_supplier, key, value)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def delete_supplier(db: Session, supplier_id: int):
    db_supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not db_supplier:
        return None
    db.delete(db_supplier)
    db.commit()
    return db_supplier

# Purchases
def create_purchase(db: Session, purchase: schemas.PurchaseCreate):
    db_purchase = models.Purchase(**purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

def get_purchases(db: Session):
    return db.query(models.Purchase).all()

def update_purchase(db: Session, purchase_id: int, purchase_update: schemas.PurchaseUpdate):
    db_purchase = db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()
    if not db_purchase:
        return None
    for key, value in purchase_update.dict(exclude_unset=True).items():
        setattr(db_purchase, key, value)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

def delete_purchase(db: Session, purchase_id: int):
    db_purchase = db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()
    if not db_purchase:
        return None
    db.delete(db_purchase)
    db.commit()
    return db_purchase

# Invoices
def create_invoice(db: Session, invoice: schemas.InvoiceCreate):
    db_invoice = models.Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoices(db: Session):
    return db.query(models.Invoice).all()

def update_invoice(db: Session, invoice_id: int, invoice_update: schemas.InvoiceUpdate):
    db_invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not db_invoice:
        return None
    for key, value in invoice_update.dict(exclude_unset=True).items():
        setattr(db_invoice, key, value)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def delete_invoice(db: Session, invoice_id: int):
    db_invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not db_invoice:
        return None
    db.delete(db_invoice)
    db.commit()
    return db_invoice
