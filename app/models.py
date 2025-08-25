from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)

    employees = relationship("Employee", back_populates="store")
    customers = relationship("Customer", back_populates="store")
    suppliers = relationship("Supplier", back_populates="store")
    purchases = relationship("Purchase", back_populates="store")
    invoices = relationship("Invoice", back_populates="store")

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="employees")

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="customers")

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="suppliers")

class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    description = Column(String(255))
    amount = Column(Float)
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="purchases")

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    total = Column(Float)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="invoices")
