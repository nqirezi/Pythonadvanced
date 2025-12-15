from fastapi import APIRouter, HTTPException
from typing import List
from models.category import Category, CategoryCreate, CategoryUpdate

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


categories_db = []


@router.get("/", response_model=List[Category])
def get_categories():
    return categories_db


@router.post("/", response_model=Category)
def create_category(category: CategoryCreate):
    new_category = {
        "id": len(categories_db) + 1,
        "name": category.name
    }
    categories_db.append(new_category)
    return new_category


@router.put("/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryUpdate):
    for cat in categories_db:
        if cat["id"] == category_id:
            cat["name"] = category.name
            return cat
    raise HTTPException(status_code=404, detail="Category not found")


@router.delete("/{category_id}")
def delete_category(category_id: int):
    for cat in categories_db:
        categories_db.remove(cat)
        return {"message": "Category deleted successfully"}
    raise HTTPException(status_code=404, detail="Category not found")
