import streamlit as st
from PIL import Image
import base64
api_key = "0be0be1639214b32986215885a44cde0"
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
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        height: 100px; /* Ajuster la hauteur pour centrer les boutons */
    }
    .stButton>button {
        background-color: #6A994E;
        color: #FFFFFF;
        border-radius: 15px;
        padding: 10px;  /* Padding vertical */
        margin: 0 10px;
        font-size: 18px;
        border: none;
        transition: background-color 0.3s ease;
        cursor: pointer;
        height: 100%; /* Remplir toute la hauteur de la colonne */
        width: 100%; /* Remplir toute la largeur de la colonne */
    }
    .stButton>button:hover {
        background-color: #A7C957;
    }

    .button-col {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;  /* Assurez-vous que la hauteur est suffisante */
        vertical-align: center;
        text-align: center;
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
    
    .a:link, .a:visited {
      background-color: #6A994E;
      color: #F2E8CF;
      padding: 14px 25px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      width: 100%;
    }
    
    .a:hover, a:active {
      background-color: #A7C957;
    }
    
    h1, h2, h3, h4, h5, h6, p, label {
        color: #F2E8CF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Appliquer la classe de style principale
st.markdown('<div class="main">', unsafe_allow_html=True)

# Charger l'image
image_path = "images/photo1.png"
image_base64 = get_base64_of_image(image_path)

# CSS pour positionner le texte correctement au centre de l'image avec une police plus grande
# Section d'en-tête avec l'image et le titre
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
    .button {{
        background-color: #6A994E;
        color: #FFFFFF;
        border-radius: 15px;
        padding: 10px;  /* Padding vertical */
        margin: 0 10px;
        font-size: 18px;
        border: none;
        transition: background-color 0.3s ease;
        cursor: pointer;
        height: 100%; /* Remplir toute la hauteur de la colonne */
        width: 100%; /* Remplir toute la largeur de la colonne */
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

# Section de la table des matières
st.markdown("<h1 class='markdown-text' style='text-align: center'>Table of Contents</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    image_base64 = get_base64_of_image("images/recipes.png")
    st.markdown(f"""
        <a href="#recipes" class="a">
        <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
        \nRecipe</a>
    """, unsafe_allow_html=True)

with col2:
    image_base64 = get_base64_of_image("images/mealPlan.png")
    st.markdown(f"""
        <a href="#meal-planner" class="a">
        <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
        \nMeal Planning</a>
    """, unsafe_allow_html=True)

with col3:
    image_base64 = get_base64_of_image("images/food.png")
    st.markdown(f"""
        <a href="#food-selection" class="a">
        <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
        \nFood Selection</a>
    """, unsafe_allow_html=True)

st.markdown("\n\n\n")

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


# Interface de l'application
st.markdown("<div id='recipes'></div>", unsafe_allow_html=True)
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

# Partie 6
import random

# Titre principal
st.markdown("<div id='meal-planner'></div>", unsafe_allow_html=True)
st.markdown(f"<h1 class='recipe-title' style='text-align: left;'>Meal Planning for the Week</h1>", unsafe_allow_html=True)

# Sélection du régime alimentaire via un menu déroulant où l'on peut choisir un seul régime
st.markdown("<p class='recipe-title' style='text-align: left;'>Select a Diet (optional)</p>", unsafe_allow_html=True)
selected_diet = st.selectbox(
    "",
    ["None", "Gluten Free", "Vegetarian", "Vegan", "Pescetarian"]
)


# Liste des jours de la semaine
st.markdown("<p class='recipe-title' style='text-align: left;'>Select a Day</p>", unsafe_allow_html=True)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
selected_day = st.selectbox("", days_of_week)


# Fonction pour appeler l'API Spoonacular avec le régime sélectionné
def get_meal_plan(diet):
    # Construire l'URL pour l'API
    url = f"https://api.spoonacular.com/mealplanner/generate?apiKey={api_key}&timeFrame=week"

    # Ajouter le régime à la requête s'il est sélectionné
    if diet and diet != "None":
        url += f"&diet={diet.lower()}"

    # Ajouter un paramètre aléatoire pour que l'API retourne des résultats variés
    url += f"&random={random.randint(1, 1000)}"

    # Faire la requête à l'API
    response = requests.get(url)
    return response.json()


# Si un régime est sélectionné, obtenir le plan de repas correspondant
if selected_diet:
    meal_plan_data = get_meal_plan(selected_diet)

    # Vérification des résultats
    if meal_plan_data and 'week' in meal_plan_data:
        # Obtenir les repas pour le jour sélectionné
        day_meals = meal_plan_data['week'][selected_day.lower()]['meals']

        st.markdown(f"<h4 class='recipe-title' style='text-align:left'>Meal Plan for {selected_day}</h4>", unsafe_allow_html=True)

        # Utiliser trois colonnes pour afficher le petit-déjeuner, le déjeuner et le dîner
        col1, col2, col3 = st.columns(3)

        # Afficher le petit-déjeuner dans la première colonne
        with col1:
            st.markdown(f"<h3 class='recipe-title'>Breakfast</h3>", unsafe_allow_html=True)
            meal = day_meals[0]
            st.write(f"• {meal['title']}")
            if 'imageType' in meal and meal['imageType']:
                image_url = f"https://spoonacular.com/recipeImages/{meal['id']}-312x231.{meal['imageType']}"
                st.image(image_url, use_column_width=True)
            else:
                st.write("No image available.")
            st.write(f"Ready in: {meal['readyInMinutes']} minutes" if 'readyInMinutes' in meal else "")
            st.markdown(f"""
                            <p style='text-align: center;'>
                                <a href="{meal['sourceUrl']}" class="a">
                                    View Recipe
                                </a>
                            </p>
                            """, unsafe_allow_html=True)

        # Afficher le déjeuner dans la deuxième colonne
        with col2:
            st.markdown(f"<h3 class='recipe-title'>Lunch</h3>", unsafe_allow_html=True)
            meal = day_meals[1]
            st.write(f"• {meal['title']}")
            if 'imageType' in meal and meal['imageType']:
                image_url = f"https://spoonacular.com/recipeImages/{meal['id']}-312x231.{meal['imageType']}"
                st.image(image_url, use_column_width=True)
            else:
                st.write("No image available.")
            st.write(f"Ready in: {meal['readyInMinutes']} minutes" if 'readyInMinutes' in meal else "")
            st.markdown(f"""
                <p style='text-align: center;'>
                    <a href="{meal['sourceUrl']}" class="a">
                        View Recipe
                    </a>
                </p>
                """, unsafe_allow_html=True)

        # Afficher le dîner dans la troisième colonne
        with col3:
            st.markdown(f"<h3 class='recipe-title'>Dinner</h3>", unsafe_allow_html=True)
            meal = day_meals[2]
            st.write(f"• {meal['title']}")
            if 'imageType' in meal and meal['imageType']:
                image_url = f"https://spoonacular.com/recipeImages/{meal['id']}-312x231.{meal['imageType']}"
                st.image(image_url, use_column_width=True)
            else:
                st.write("No image available.")
            st.write(f"Ready in: {meal['readyInMinutes']} minutes" if 'readyInMinutes' in meal else "")
            st.markdown(f"""
                            <p style='text-align: center;'>
                                <a href="{meal['sourceUrl']}" class="a">
                                    View Recipe
                                </a>
                            </p>
                            """, unsafe_allow_html=True)


    else:
        st.write("No meal plan data available. Please try different filters.")
else:
    st.write("Please select a diet to generate a meal plan.")

# Titre principal
st.markdown("<div id='food-selection'></div>", unsafe_allow_html=True)
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

