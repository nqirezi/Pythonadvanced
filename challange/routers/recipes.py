from models.recipe import Recipe, RecipeCreate
import database


def category_exists(category_id: int) -> bool:
    return any(cat.id == category_id for cat in database.categories_db)

def get_recipes(cuisine: str = None, difficulty: str = None):
    results = database.recipes_db

    if cuisine:
        results = [r for r in results if r.cuisine == cuisine]

    if difficulty:
        results = [r for r in results if r.difficulty == difficulty]

    return results

def create_recipe(recipe: RecipeCreate):
    if recipe.category_id and not category_exists(recipe.category_id):
        return None

    new_recipe = Recipe(
        id=len(database.recipes_db) + 1,
        **recipe.dict()
    )
    database.recipes_db.append(new_recipe)
    return new_recipe

def update_recipe(recipe_id: int, recipe: RecipeCreate):
    for r in database.recipes_db:
        if r.id == recipe_id:
            for key, value in recipe.dict().items():
                setattr(r, key, value)
            return r
    return None

def delete_recipe(recipe_id: int):
    for r in database.recipes_db:
        if r.id == recipe_id:
            database.recipes_db.remove(r)
            return {"message": "Recipe deleted"}
    return {"message": "Recipe not found"}
