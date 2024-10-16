import streamlit as st
from PIL import Image
import base64

# Activer la mise en page large
st.set_page_config(layout="wide")

def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Ajouter un style CSS pour changer la couleur de fond, la couleur du texte et le style des boutons
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

    /* Styles spécifiques pour centrer les boutons dans chaque colonne */
    .button-col {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;  /* Assurez-vous que la hauteur est suffisante */
        vertical-align: center;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Fonction pour exécuter et afficher le contenu d'un fichier Python
def execute_python_file(filepath):
    try:
        with open(filepath, 'r') as file:
            file_content = file.read()
            exec(file_content, globals())  # Exécution du contenu du fichier
    except Exception as e:
        st.error(f"Erreur lors de l'exécution du fichier {filepath}: {e}")

# Gestion de la logique des boutons
if "page" not in st.session_state:
    st.session_state.page = "home"  # Définir la page d'accueil par défaut

# Logique de navigation
if st.session_state.page == "home":
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
            <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
        """, unsafe_allow_html=True)

    with col2:
        image_base64 = get_base64_of_image("images/mealPlan.png")
        st.markdown(f"""
            <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
        """, unsafe_allow_html=True)

    with col3:
        image_base64 = get_base64_of_image("images/food.png")
        st.markdown(f"""
            <img src="data:image/png;base64,{image_base64}" style='border-radius: 25px; max-width: 100%; height: auto;'>
        """, unsafe_allow_html=True)

    # Afficher les boutons de navigation sur la page d'accueil avec un style différent
    st.markdown('<div class="home-button-container">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    # Ajouter une classe CSS pour centrer les boutons dans leur colonne
    with col1:
        st.markdown('<div class="button-col">', unsafe_allow_html=True)
        recipes = st.button("Recipes")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="button-col">', unsafe_allow_html=True)
        mealPlan = st.button("Meal Planner")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="button-col">', unsafe_allow_html=True)
        foodSelection = st.button("Food Selection")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Changer de page si un bouton est cliqué
    if recipes:
        st.session_state.page = "recipes"
    elif mealPlan:
        st.session_state.page = "mealPlan"
    elif foodSelection:
        st.session_state.page = "foodSelection"

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

else:
    # Afficher les boutons normalement sur les autres pages
    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        st.markdown('<div class="button-col">', unsafe_allow_html=True)
        recipes = st.button("Recipes")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="button-col">', unsafe_allow_html=True)
        mealPlan = st.button("Meal Planner")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="button-col">', unsafe_allow_html=True)
        foodSelection = st.button("Food Selection")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="button-col">', unsafe_allow_html=True)
        main = st.button("Retour à la page principale")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Gestion du contenu de la page
    if recipes:
        execute_python_file("./recipes.py")
    elif mealPlan:
        execute_python_file("./mealPlan.py")
    elif foodSelection:
        execute_python_file("./food_selection.py")
    elif main:
        st.session_state.page = "home"
