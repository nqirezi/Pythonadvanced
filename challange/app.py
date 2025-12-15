from models.category import Category, CategoryCreate, CategoryUpdate
from models.recipe import RecipeCreate
import database


def get_categories():
    return database.categories_db

def create_category(category: CategoryCreate):
    cat = Category(
        id=database.category_id_counter,
        name=category.name
    )
    database.categories_db.append(cat)
    database.category_id_counter += 1
    return cat

def update_category(category_id: int, category: CategoryUpdate):
    for cat in database.categories_db:
        if cat.id == category_id:
            cat.name = category.name
            return cat
    return None

def delete_category(category_id: int):
    for cat in database.categories_db:
        if cat.id == category_id:
            database.categories_db.remove(cat)
            return True
    return False


def get_recipes():
    return database.recipes_db

def create_recipe(recipe: RecipeCreate):
    if recipe.category_id is not None:
        if not any(c.id == recipe.category_id for c in database.categories_db):
            return None
    new_recipe = {
        "id": database.recipe_id_counter,
        "name": recipe.name,
        "description": recipe.description,
        "ingredients": recipe.ingredients,
        "instructions": recipe.instructions,
        "cuisine": recipe.cuisine,
        "difficulty": recipe.difficulty,
        "category_id": recipe.category_id
    }
    database.recipes_db.append(new_recipe)
    database.recipe_id_counter += 1
    return new_recipe
