from fastapi import FastAPI
from database import engine
import models
from routers import users, products

# This creates all tables in PostgreSQL automatically!
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Project",
    description="A complete REST API with PostgreSQL",
    version="1.0.0"
)

# Register routers
app.include_router(users.router)
app.include_router(products.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with PostgreSQL!"}