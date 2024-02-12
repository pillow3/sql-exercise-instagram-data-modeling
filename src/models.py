import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



# INSTAGRAM
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    pricing = Column(Float, nullable=False)
    weight = Column(Float, nullable=True)
    color = Column(String(100), nullable=True)
    
    shopping_cart_items = relationship("ShoppingCart", back_populates='product')

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    address = Column(String(250), nullable=True)

    shopping_cart = relationship("ShoppingCart", back_populates='customer')


class Bill(Base):
    __tablename__ = 'bill'
    id = Column(Integer, primary_key=True)
    created_at = Column(Date)
    total_price = Column(Float, nullable=False)
    status = Column(Enum('PAID', 'PENDING', 'REFUNDED'))

    shopping_carts = relationship("ShoppingCart", back_populates='bill')

class ShoppingCart(Base):
    __tablename__ = 'shoppingcart'

    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    customer_id = Column(Integer,ForeignKey('customer.id'), primary_key=True )
    quantity = Column(Integer)
    price = Column(Float)
    bill_id = Column(Integer, ForeignKey('bill.id'))

    product = relationship("Product", back_populates="shopping_cart_items")
    customer = relationship("Customer", back_populates="shopping_carts")
    bill = relationship("Bill", back_populates="shopping_carts")



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
