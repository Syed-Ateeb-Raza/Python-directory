from fastapi import APIRouter
from typing import Optional

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products(category: str, limit: int = 10, search: Optional[str] = None):
    return {
        "category": category,
        "limit": limit,
        "search": search,
        "message": f"Showing {limit} products from {category} category"
    }


@router.post("/")
def create_product(name: str, price: float, category: str):
    return {
        "message": "Product created successfully!",
        "product": {
            "name": name,
            "price": price,
            "category": category
        }
    }