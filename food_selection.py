import streamlit as st
from PIL import Image
import requests
import base64


# Ajouter un style CSS pour changer la couleur de fond, la couleur du texte et le style des images
st.markdown("""
    <style>
    .main {
        background-color: #386641;
        color: #F2E8CF;
    }
    .markdown-text {
        color: #F2E8CF;
    }

    </style>
    """, unsafe_allow_html=True)

# Appliquer la classe de style principale
st.markdown('<div class="main">', unsafe_allow_html=True)

api_key = "0e85d9946e0f45d3a9df7ef93302aef1"

# Titre principal
st.markdown("<h1 style='color: #F2E8CF' id='food-selection'>Food-selection</h1>", unsafe_allow_html=True)

# Dictionnaire pour stocker les sélections
selected_foods = {
    "Vegetables": [],
    "Protein (Meat & Plant-Based)": [],
    "Grains": [],
    "Fruits": [],
    "Nuts & Seeds": [],
    "Seafood": [],
    "Dairy": [],
    "Legumes": [],
    "Cuisines": [],
    "Meal Types": [],
    "Diets": []
}

# Utiliser des menus déroulants pour organiser les filtres
with st.expander("Vegetables"):
    for i, vegetable in enumerate(["Carrot", "Broccoli", "Spinach", "Kale", "Bell Peppers", "Zucchini"]):
        if st.checkbox(vegetable, key=f'vegetable_{i}'):
            selected_foods["Vegetables"].append(vegetable)

with st.expander("Protein (Meat & Plant-Based)"):
    for i, protein in enumerate(["Chicken", "Lentils", "Tofu", "Beef", "Pork", "Eggs"]):
        if st.checkbox(protein, key=f'protein_{i}'):
            selected_foods["Protein (Meat & Plant-Based)"].append(protein)

with st.expander("Grains"):
    for i, grain in enumerate(["Rice", "Quinoa", "Oats", "Barley", "Couscous"]):
        if st.checkbox(grain, key=f'grain_{i}'):
            selected_foods["Grains"].append(grain)

with st.expander("Fruits"):
    for i, fruit in enumerate(["Apple", "Banana", "Orange", "Blueberries", "Strawberries", "Mango"]):
        if st.checkbox(fruit, key=f'fruit_{i}'):
            selected_foods["Fruits"].append(fruit)

with st.expander("Nuts & Seeds"):
    for i, nut_seed in enumerate(["Almonds", "Chia seeds", "Sunflower seeds", "Cashews", "Peanuts"]):
        if st.checkbox(nut_seed, key=f'nut_seed_{i}'):
            selected_foods["Nuts & Seeds"].append(nut_seed)

with st.expander("Seafood"):
    for i, seafood in enumerate(["Salmon", "Shrimp", "Tuna", "Cod", "Scallops"]):
        if st.checkbox(seafood, key=f'seafood_{i}'):
            selected_foods["Seafood"].append(seafood)

with st.expander("Dairy"):
    for i, dairy in enumerate(["Milk", "Cheese", "Yogurt", "Butter", "Cream"]):
        if st.checkbox(dairy, key=f'dairy_{i}'):
            selected_foods["Dairy"].append(dairy)

with st.expander("Legumes"):
    for i, legume in enumerate(["Chickpeas", "Black beans", "Green peas", "Lentils", "Soybeans"]):
        if st.checkbox(legume, key=f'legume_{i}'):
            selected_foods["Legumes"].append(legume)

with st.expander("Cuisines"):
    for i, cuisine in enumerate(["Italian", "Mexican", "Chinese", "Indian", "French", "Japanese"]):
        if st.checkbox(cuisine, key=f'cuisine_{i}'):
            selected_foods["Cuisines"].append(cuisine)

with st.expander("Meal Types"):
    for i, meal in enumerate(["Breakfast", "Lunch", "Dinner", "Snack", "Dessert"]):
        if st.checkbox(meal, key=f'meal_{i}'):
            selected_foods["Meal Types"].append(meal)

with st.expander("Diets"):
    for i, diet in enumerate(["Gluten Free", "Ketogenic", "Vegetarian", "Vegan", "Paleo", "Pescatarian"]):
        if st.checkbox(diet, key=f'diet_{i}'):
            selected_foods["Diets"].append(diet)


# Fonction pour appeler l'API Spoonacular en fonction des aliments sélectionnés
def get_recipes_based_on_foods(selected_foods):
    # Combine toutes les sélections d'ingrédients dans une chaîne de caractères
    ingredients = []
    for category, items in selected_foods.items():
        ingredients.extend(items)

    # Créer une chaîne avec les ingrédients séparés par des virgules
    ingredient_query = ','.join(ingredients)

    # Faire une requête à l'API pour obtenir les recettes basées sur les ingrédients
    if ingredient_query:
        url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredient_query}&number=6&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()
        return data
    else:
        return []


# Si l'utilisateur a sélectionné des aliments, appeler l'API et afficher les résultats
if any(selected_foods.values()):  # Vérifier si des aliments ont été sélectionnés
    st.subheader("Selected Recipes")
    recipes = get_recipes_based_on_foods(selected_foods)

    # Afficher les recettes dans une grille
    col1, col2, col3 = st.columns(3)
    for idx, recipe in enumerate(recipes):
        if idx % 3 == 0:
            with col1:
                st.image(recipe['image'], caption=recipe['title'])
        elif idx % 3 == 1:
            with col2:
                st.image(recipe['image'], caption=recipe['title'])
        else:
            with col3:
                st.image(recipe['image'], caption=recipe['title'])

st.markdown('</div>', unsafe_allow_html=True)