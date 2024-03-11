from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# DB URL
database_url = 'mysql+pymysql://root:Agus2003Jazm2008@localhost:3306/DOTASYS'  # TODO ocultar password

# Engine Connection
engine = create_engine(database_url)

# Base
Base = declarative_base()


# Employee class
class Employee(Base):
    __tablename__ = 'employee'
    employee_ID = Column(Integer, primary_key=True, nullable=False)  # PK
    employee_username = Column(String(8), nullable=False)
    password = Column(String(200), nullable=False)


# Manager class
class Manager(Base):
    __tablename__ = 'manager'
    manager_ID = Column(Integer, primary_key=True, nullable=False)  # PK
    manager_username = Column(String(20), nullable=False)
    password = Column(String(200), nullable=False)


# Product class
class Product(Base):
    __tablename__ = 'product'

    product_barcode = Column(Integer, primary_key=True, nullable=False)  # PK
    employee_ID = Column(Integer, ForeignKey('employee.employee_ID'), nullable=False)  # FK
    product_name = Column(String(60), nullable=False)
    product_brand = Column(String(60), nullable=False)
    stock = Column(Integer, default=0)

    # Relationships
    employee = relationship("Employee")

    def __str__(self):
        return f"{self.product_barcode},{self.product_name},{self.product_brand},{self.stock}"

    # hace que se imprima __str__ bien
    __repr__ = __str__


# Supplier class
class Supplier(Base):
    __tablename__ = 'supplier'

    supplier_ID = Column(Integer, primary_key=True, nullable=False)  # PK
    supplier_name = Column(String(60), nullable=False)
    address = Column(String(60), nullable=False)
    contact = Column(String(60), nullable=False)


# PurchaseOrder class
class PurchaseOrder(Base):
    __tablename__ = 'purchase_order'

    purchase_order_ID = Column(Integer, primary_key=True, nullable=False)  # PK
    product_barcode = Column(Integer, ForeignKey('product.product_barcode'), nullable=False)  # FK
    supplier_ID = Column(Integer, ForeignKey('supplier.supplier_ID'), nullable=False)  # FK
    manager_ID = Column(Integer, ForeignKey('manager.manager_ID'), nullable=False)  # FK
    order_date = Column(DateTime, nullable=False)
    amount = Column(Integer, nullable=False)
    total_price = Column(Integer, nullable=False)

    # Relationships
    product = relationship("Product")
    supplier = relationship("Supplier")
    manager = relationship("Manager")


# SupplierProduct class
class SupplierProduct(Base):
    __tablename__ = 'supplier_product'

    supplier_product_ID = Column(Integer, primary_key=True, nullable=False)  # PK
    product_barcode = Column(Integer, ForeignKey('product.product_barcode'), nullable=False)  # FK
    supplier_ID = Column(Integer, ForeignKey('supplier.supplier_ID'), nullable=False)  # FK
    unit_price = Column(Integer, nullable=False)

    # Relationships
    product = relationship("Product")
    supplier = relationship("Supplier")


# Creating tables
Base.metadata.create_all(engine)

# Inserting data
session = sessionmaker(bind=engine)
new_session = session()

new_session.close()
