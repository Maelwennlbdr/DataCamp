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
    .recipe-title {
        color: #F2E8CF;
        text-align: center;
    }
    .image-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;  /* Pour assurer un bon alignement */
    }
    .recipe {
        margin: 10px;  /* Espacement entre les recettes */
    }
    </style>
    """, unsafe_allow_html=True)

# Appliquer la classe de style principale
st.markdown('<div class="main">', unsafe_allow_html=True)

def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_path = "images/about.png"
image_base64 = get_base64_of_image(image_path)
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
api_key = "0e85d9946e0f45d3a9df7ef93302aef1"

# Interface de l'application
st.markdown("<h1 style='color: #F2E8CF'>Recipes</h1>", unsafe_allow_html=True)

# Régimes alimentaires disponibles dans l'API Spoonacular
diet_options = [
    "None",  # Option pour indiquer qu'aucun régime alimentaire n'est sélectionné
    "Gluten Free", "Ketogenic", "Vegetarian", "Lacto-Vegetarian", "Ovo-Vegetarian",
    "Vegan", "Pescetarian", "Paleo", "Primal", "Whole30"
]

# Nouvelles tranches de calories
calorie_options = ["Moins de 200", "200-500", "500-700", "Plus de 700"]

# Organiser les filtres en menus déroulants
with st.expander("Select a diet (optional)"):
    selected_diet = st.selectbox("", diet_options)

with st.expander("Select a calorie range"):
    selected_calories = st.selectbox("", calorie_options)

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

# Fonction pour obtenir les détails de la recette
def get_recipe_details(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Si un régime ou une tranche de calories sont sélectionnés, afficher les recettes correspondantes
if selected_calories:
    st.markdown(f"<h3 style='color: #F2E8CF'>Recipes with {selected_calories} calories</h3>", unsafe_allow_html=True)
    recipes = get_recipes_for_diet_and_calories(selected_diet.lower(), selected_calories)

    # Créer autant de colonnes que de recettes à afficher (ici 3 pour la mise en page)
    cols = st.columns(3)

    for idx, recipe in enumerate(recipes):
        recipe_id = recipe['id']
        col_index = idx % 3  # Détermine la colonne à utiliser

        with cols[col_index]:
            st.image(recipe['image'], use_column_width=True)
            st.markdown(f"<h4 class='recipe-title'>{recipe['title']}</h4>", unsafe_allow_html=True)

            if st.button(f"View Recipe {idx + 1}", key=f"button_{idx}"):
                # Obtenir les détails de la recette et les afficher dans un expander
                details = get_recipe_details(recipe_id)
                with st.expander(f"Recipe Details for {recipe['title']}"):
                    st.image(details['image'], caption=details['title'])
                    st.write(f"**Servings**: {details['servings']}")
                    st.write(f"**Ready in**: {details['readyInMinutes']} minutes")
                    instructions = details['instructions'] if details['instructions'] else "No instructions available."
                    st.write(instructions)

st.markdown('</div>', unsafe_allow_html=True)
