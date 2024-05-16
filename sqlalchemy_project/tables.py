import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapped_column


from sqlalchemy_project.constants import URL

engine = create_engine(URL)
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product = Column(String)
    price = Column('price_eur', Float)
    ingredients = Column(Text)
    extra = Column(String)
    order = relationship("Order", back_populates="product")

    def __init__(self, product, price, ingredients, extra=''):
        self.product = product
        self.price = price
        self.ingredients = ingredients
        self.extra = extra

    def __repr__(self):
        return f"{self.product_id} {self.product} - {self.price}"


class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    order_customer = relationship("Order", back_populates="customer_order")

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return f"{self.name} {self.phone_number}"


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)

    product_id = mapped_column(ForeignKey('products.product_id'))
    product = relationship("Product", back_populates="order")

    customer_id = mapped_column(ForeignKey('customers.customer_id'))
    customer_order = relationship("Customer", back_populates="order_customer")

    quantity = Column(String)
    order_time = Column(String, default=datetime.datetime.now)

    def __init__(self, customer_id, product_id, quantity):
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"Oder_id: {self.order_id}, product_id: {self.product_id} " \
               f"customer_id: {self.customer_id};"


Base.metadata.create_all(engine)
