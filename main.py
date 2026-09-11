from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Products
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=['*']
)


database_models.base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to FastAPI framework"

products = [
    Products(id=1, name="phone", description="A smartphone", price=699.99, quantity=50),
    Products(id=2, name="laptop", description="A powerful laptop", price=999.99, quantity=30),
    Products(id=3, name="pen", description="A Blue ink pen", price=1.99, quantity=100),
    Products(id=4, name="Table", description="A wooden table", price=199.99, quantity=20)
]

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db=session()
    count=db.query(database_models.Products).count
    if count==0:
        for product in products:
            db.add(database_models.Products(**product.model_dump()))
        db.commit()
init_db()

@app.get("/products")
def get_all_products(db:Session=Depends(get_db)):
    # db = session()
    db_products=db.query(database_models.Products).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int,db:Session=Depends(get_db)):
    db_products=db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_products:
        return db_products
    return {"message": "product Not Found"}

@app.post("/products")
def add_product(product: Products,db:Session=Depends(get_db)):
    db.add(database_models.Products(**product.model_dump()))
    db.commit()


@app.put("/products/{id}")
def update_product(id: int, product: Products,db:Session=Depends(get_db)):
    db_products=db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_products:
        db_products.name=product.name
        db_products.description=product.description
        db_products.price=product.price
        db_products.quantity=product.quantity
        db.commit()
    else:
        "product not found"



@app.delete("/products/{id}")
def delete_product(id: int,db:Session=Depends(get_db)):
    db_products=db.query(database_models.Products).filter(database_models.Products.id==id).first()
    if db_products:
        db.delete(db_products)
        db.commit()
        return {"message": "products deleted successfully"}
    else:
        return {"message": "product not found"}

