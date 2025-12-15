import streamlit as st
from models.category import CategoryCreate
from models.recipe import RecipeCreate
import app

st.set_page_config(page_title="Recipe App", layout="wide")
st.title(" Recipe Management App")

menu = st.sidebar.selectbox("Menu", ["Categories", "Recipes"])

if menu == "Categories":
    st.header("Categories")

    name = st.text_input("Category name")
    if st.button("Add Category"):
        app.create_category(CategoryCreate(name=name))
        st.success("Category added")

    st.subheader("All Categories")
    for cat in app.get_categories():
        st.write(f"{cat.id}. {cat.name}")

if menu == "Recipes":
    st.header("Recipes")
    categories = app.get_categories()
    category_map = {c.name: c.id for c in categories}

    name = st.text_input("Recipe name")
    description = st.text_area("Description")
    ingredients = st.text_area("Ingredients")
    instructions = st.text_area("Instructions")
    cuisine = st.text_input("Cuisine")
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    category_name = st.selectbox("Category", ["None"] + list(category_map.keys()))
    category_id = category_map.get(category_name)

    if st.button("Add Recipe"):
        recipe = RecipeCreate(
            name=name,
            description=description,
            ingredients=ingredients,
            instructions=instructions,
            cuisine=cuisine,
            difficulty=difficulty,
            category_id=category_id
        )
        result = app.create_recipe(recipe)
        if result:
            st.success("Recipe added")
        else:
            st.error("Category does not exist")

    st.subheader("All Recipes")
    for r in app.get_recipes():
        st.markdown(f"""
        ### {r['name']}
        **Cuisine:** {r['cuisine']}  
        **Difficulty:** {r['difficulty']}  
        **Ingredients:** {r['ingredients']}
        """)
