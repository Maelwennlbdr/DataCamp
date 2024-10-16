import streamlit as st
import requests

st.set_page_config(page_title="Recipes", layout="wide")

api_key = "0e85d9946e0f45d3a9df7ef93302aef1"

# Interface de recettes
st.title("Recipes")

# Régimes alimentaires et tranches de calories
diet_options = ["None", "Gluten Free", "Ketogenic", "Vegetarian", "Vegan"]
calorie_options = ["Moins de 200", "200-500", "500-700", "Plus de 700"]

# Sélection des filtres
selected_diet = st.selectbox("Choose a diet", diet_options)
selected_calories = st.selectbox("Select calorie range", calorie_options)

# Fonction pour obtenir des recettes
def get_recipes(diet, calories):
    url = f"https://api.spoonacular.com/recipes/complexSearch?diet={diet}&apiKey={api_key}&number=6"
    response = requests.get(url)
    return response.json()["results"]

if st.button("Show Recipes"):
    recipes = get_recipes(selected_diet, selected_calories)
    col1, col2, col3 = st.columns(3)
    for idx, recipe in enumerate(recipes):
        with [col1, col2, col3][idx % 3]:
            st.image(recipe["image"], caption=recipe["title"])
