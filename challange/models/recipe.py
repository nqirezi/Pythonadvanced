from pydantic import BaseModel
from typing import Optional

class RecipeCreate(BaseModel):
    name: str
    description: str
    ingredients: str
    instructions: str
    cuisine: str
    difficulty: str
    category_id: Optional[int]
