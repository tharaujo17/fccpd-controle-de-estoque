from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
from typing import List
from sqlalchemy import func

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Controle de Estoque de Doceria")

# Endpoints de Fornecedores
@app.post("/fornecedores/", response_model=schemas.Supplier)
def criar_fornecedor(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = models.Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@app.get("/fornecedores/", response_model=List[schemas.Supplier])
def listar_fornecedores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suppliers = db.query(models.Supplier).offset(skip).limit(limit).all()
    return suppliers

# Endpoints de Ingredientes
@app.post("/ingredientes/", response_model=schemas.Ingredient)
def criar_ingrediente(ingredient: schemas.IngredientCreate, db: Session = Depends(get_db)):
    db_ingredient = models.Ingredient(**ingredient.dict())
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

@app.get("/ingredientes/", response_model=List[schemas.Ingredient])
def listar_ingredientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ingredients = db.query(models.Ingredient).offset(skip).limit(limit).all()
    return ingredients

@app.get("/ingredientes/estoque-baixo", response_model=List[schemas.Ingredient])
def obter_ingredientes_estoque_baixo(db: Session = Depends(get_db)):
    return db.query(models.Ingredient).filter(
        models.Ingredient.quantity <= models.Ingredient.min_stock
    ).all()

# Endpoints de Movimentação de Estoque
@app.post("/movimentacoes/", response_model=schemas.StockMovement)
def criar_movimentacao(movement: schemas.StockMovementCreate, db: Session = Depends(get_db)):
    db_movement = models.StockMovement(**movement.dict())
    
    # Atualiza quantidade do ingrediente
    ingredient = db.query(models.Ingredient).filter(models.Ingredient.id == movement.ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingrediente não encontrado")
    
    if movement.movement_type == "ENTRADA":
        ingredient.quantity += movement.quantity
    else:
        if ingredient.quantity < movement.quantity:
            raise HTTPException(status_code=400, detail="Estoque insuficiente")
        ingredient.quantity -= movement.quantity
    
    db.add(db_movement)
    db.commit()
    db.refresh(db_movement)
    return db_movement

@app.get("/movimentacoes/", response_model=List[schemas.StockMovement])
def listar_movimentacoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movements = db.query(models.StockMovement).offset(skip).limit(limit).all()
    return movements