import streamlit as st
from PIL import Image
import base64

# Activer la mise en page large
st.set_page_config(layout="wide")

def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

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

# Charger l'image
image_path = "images/photo1.png"
image_base64 = get_base64_of_image(image_path)

# CSS pour positionner le texte correctement au centre de l'image avec une police plus grande
st.markdown(
    f"""
    <style>
    .image-container {{
        position: relative;
        width: 100%;
        max-width: 100%;
        text-align: center;
        color: white;
    }}
    .image {{
        width: 100%;
        height: auto;
    }}
    .centered-text {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 120px;  /* Augmenter la taille de la police pour le titre */
        font-weight: bold;
        color: #F2E8CF;
    }}
    .centered-text span {{
        font-size: 32px;  /* Augmenter la taille de la police pour le sous-titre */
    }}
    </style>

    <div class="image-container">
        <img src="data:image/png;base64,{image_base64}" class="image">
        <div class="centered-text">
            PlateMate<br>
            <span>PROJET DATACAMP</span>
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Table of contents section
st.markdown("<h1 class='markdown-text' style='text-align: center'>Table of Contents</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    image_base64 = get_base64_of_image("images/recipes.png")
    st.markdown(f"""
        <a href="#recipes" style="text-decoration: none;">
            <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
            <h3 class='markdown-text' style='text-align: center'>Recipe</h3>
        </a>
    """, unsafe_allow_html=True)

with col2:
    image_base64 = get_base64_of_image("images/mealPlan.png")
    st.markdown(f"""
        <a href="#Meal Planner" style="text-decoration: none;">
            <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
            <h3 class='markdown-text' style='text-align: center'>Meal Planning</h3>
        </a>
    """, unsafe_allow_html=True)

with col3:
    image_base64 = get_base64_of_image("images/food.png")
    st.markdown(f"""
        <a href="#Food selection" style="text-decoration: none;">
            <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
            <h3 class='markdown-text' style='text-align: center'>Food Selection</h3>
        </a>
    """, unsafe_allow_html=True)


# Charger l'image
image_path = "images/about.png"
image_base64 = get_base64_of_image(image_path)

col21, col22 = st.columns(2)
with col21:
    # Centrer l'image avec un style CSS
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
        </div>
    """, unsafe_allow_html=True)

with col22:
    st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%;">
            <h2 class='markdown-text'>About PlateMate</h2>
            <span class='markdown-text' style='text-align: center; margin: 20px;'>
                The goal of PlateMate is to simplify daily meal management by providing 
                a visual, easy-to-use meal planner for healthy eating, along with precise 
                calculations of calories for each meal.
                Users will be able to filter recipes according to their dietary preferences 
                and health concerns, including vegetarian, low-carb, and gluten-free options. 
                PlateMate provides a wide selection of nutritious, balanced recipes that 
                cater to all kinds of dietary requirements.
            </span>
        </div>
    """, unsafe_allow_html=True)


st.markdown("\n\n")
# Partie 4

# Charger l'image
image = Image.open("images/photo2.jpeg")

# Création de deux colonnes pour la mise en page
col1, col2 = st.columns([1, 1])  # Deux colonnes de même taille

with col1:
    st.markdown(
        "<h1 style='text-align: center; font-size: 60px; color: #F2E8CF; margin-top: 100px;'>Choose the perfect recipes</h1>",
        unsafe_allow_html=True)
    st.markdown(
        "<h2 style='text-align: center; font-size: 60px; color: #F2E8CF; margin-top: 20px;'>for you with the numerous filters!</h2>",
        unsafe_allow_html=True)
with col2:
    # Afficher l'image dans la première colonne
    st.image(image, use_column_width=True)


# Partie 5

import requests

# Clé d'API pour Spoonacular (à remplacer par ta propre clé)
api_key = "0be0be1639214b32986215885a44cde0"
url = f"https://api.spoonacular.com/recipes/complexSearch?query=diet&number=6&apiKey={api_key}"


def get_recipes(query):
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=6&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['results']


# Régimes alimentaires disponibles dans l'API Spoonacular
diet_options = [
    "None",  # Option pour indiquer qu'aucun régime alimentaire n'est sélectionné
    "Gluten Free", "Ketogenic", "Vegetarian", "Lacto-Vegetarian", "Ovo-Vegetarian",
    "Vegan", "Pescetarian", "Paleo", "Primal", "Whole30"
]

# Nouvelles tranches de calories
calorie_options = ["Moins de 200", "200-500", "500-700", "Plus de 700"]

# Interface de l'application
st.markdown("<h2>Recipes</h2>", unsafe_allow_html=True)

# Sélection des régimes alimentaires avec une option "None"
selected_diet = st.selectbox("Select a diet (optional)", diet_options)

# Sélection des calories
selected_calories = st.selectbox("Select a calorie range", calorie_options)


# Fonction pour appeler l'API Spoonacular et obtenir des recettes en fonction du régime et des calories
def get_recipes_for_diet_and_calories(diet, calories):
    # Définir la tranche de calories
    if calories == "Moins de 200":
        min_cal = 0
        max_cal = 200
    elif calories == "200-500":
        min_cal = 200
        max_cal = 500
    elif calories == "500-700":
        min_cal = 500
        max_cal = 700
    else:  # "Plus de 700"
        min_cal = 700
        max_cal = 10000  # Mettre une grande valeur pour inclure toutes les recettes au-dessus de 700

    # Si aucun régime n'est sélectionné, ne pas inclure le paramètre diet
    if diet == "None":
        url = f"https://api.spoonacular.com/recipes/complexSearch?minCalories={min_cal}&maxCalories={max_cal}&number=6&apiKey={api_key}"
    else:
        url = f"https://api.spoonacular.com/recipes/complexSearch?diet={diet}&minCalories={min_cal}&maxCalories={max_cal}&number=6&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()
    return data['results']


# Si un régime ou une tranche de calories sont sélectionnés, afficher les recettes correspondantes
if selected_calories:
    st.subheader(f"Recipes with {selected_calories} calories")
    recipes = get_recipes_for_diet_and_calories(selected_diet.lower(), selected_calories)
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


# Fermer la div principale
st.markdown('</div>', unsafe_allow_html=True)