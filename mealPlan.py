import streamlit as st
import requests
import random

# Appliquer un style CSS pour changer les couleurs et le design
st.markdown("""
    <style>
    .main {
        background-color: #386641;
        color: #F2E8CF;
        padding: 20px;
        border-radius: 10px;
    }

    h1 {
        color: #F2E8CF;
        font-family: 'Arial', sans-serif;
    }

    label {
        color: #F2E8CF !important;
    }

    .stSelectbox {
        color: #000;
        background-color: #f2e8cf;
        padding: 5px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Appliquer la classe de style principale
st.markdown('<div class="main">', unsafe_allow_html=True)

# Clé d'API pour Spoonacular (à remplacer par ta propre clé)
api_key = "6a782f6af3be4da4afb16a74a23e316f"

# Titre principal
st.markdown("<h1 style='text-align: center;'>Meal Planning for the Week</h1>", unsafe_allow_html=True)

# Sélection du régime alimentaire via un menu déroulant où l'on peut choisir un seul régime
selected_diet = st.selectbox(
    "Select a diet (optional)",
    ["None", "Gluten Free", "Vegetarian", "Vegan", "Pescetarian"]
)

# Liste des jours de la semaine
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
selected_day = st.selectbox("Select a day", days_of_week)

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
        
        st.subheader(f"Meal Plan for {selected_day}")

        # Utiliser trois colonnes pour afficher le petit-déjeuner, le déjeuner et le dîner
        col1, col2, col3 = st.columns(3)

        # Afficher le petit-déjeuner dans la première colonne
        with col1:
            st.markdown("### Breakfast")
            meal = day_meals[0]
            st.write(f"• {meal['title']}")
            if 'imageType' in meal and meal['imageType']:
                image_url = f"https://spoonacular.com/recipeImages/{meal['id']}-312x231.{meal['imageType']}"
                st.image(image_url, caption=meal['title'], use_column_width=True)
            else:
                st.write("No image available.")
            st.write(f"Ready in: {meal['readyInMinutes']} minutes" if 'readyInMinutes' in meal else "")
            st.write(f"[View Recipe]({meal['sourceUrl']})")

        # Afficher le déjeuner dans la deuxième colonne
        with col2:
            st.markdown("### Lunch")
            meal = day_meals[1]
            st.write(f"• {meal['title']}")
            if 'imageType' in meal and meal['imageType']:
                image_url = f"https://spoonacular.com/recipeImages/{meal['id']}-312x231.{meal['imageType']}"
                st.image(image_url, caption=meal['title'], use_column_width=True)
            else:
                st.write("No image available.")
            st.write(f"Ready in: {meal['readyInMinutes']} minutes" if 'readyInMinutes' in meal else "")
            st.write(f"[View Recipe]({meal['sourceUrl']})")

        # Afficher le dîner dans la troisième colonne
        with col3:
            st.markdown("### Dinner")
            meal = day_meals[2]
            st.write(f"• {meal['title']}")
            if 'imageType' in meal and meal['imageType']:
                image_url = f"https://spoonacular.com/recipeImages/{meal['id']}-312x231.{meal['imageType']}"
                st.image(image_url, caption=meal['title'], use_column_width=True)
            else:
                st.write("No image available.")
            st.write(f"Ready in: {meal['readyInMinutes']} minutes" if 'readyInMinutes' in meal else "")
            st.write(f"[View Recipe]({meal['sourceUrl']})")

    else:
        st.write("No meal plan data available. Please try different filters.")
else:
    st.write("Please select a diet to generate a meal plan.")
st.markdown('</div>', unsafe_allow_html=True)
