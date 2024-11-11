from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Supplier(Base):
    __tablename__ = "fornecedores"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact = Column(String)
    email = Column(String, unique=True)
    ingredients = relationship("Ingredient", back_populates="supplier")

class Ingredient(Base):
    __tablename__ = "ingredientes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    min_stock = Column(Float)
    supplier_id = Column(Integer, ForeignKey("fornecedores.id"))
    supplier = relationship("Supplier", back_populates="ingredients")
    stock_movements = relationship("StockMovement", back_populates="ingredient")

class StockMovement(Base):
    __tablename__ = "movimentacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    ingredient_id = Column(Integer, ForeignKey("ingredientes.id"))
    movement_type = Column(String)  # "ENTRADA" ou "SAÍDA"
    quantity = Column(Float)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    ingredient = relationship("Ingredient", back_populates="stock_movements")