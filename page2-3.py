import streamlit as st
import requests

# Activer la mise en page large
st.set_page_config(layout="wide")

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

# Table of contents section
st.markdown("<h1 class='markdown-text', style='text-align: center'>Table of Contents</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/recipes.png", use_column_width=True, clamp=True)
    st.markdown("<h3 class='markdown-text', style='text-align: center'>Recipes</h3>", unsafe_allow_html=True)
with col2:
    st.image("images/mealPlan.png", use_column_width=True, clamp=True)
    st.markdown("<h3 class='markdown-text', style='text-align: center'>Meal Planning</h3>", unsafe_allow_html=True)
with col3:
    st.image("images/food.png", use_column_width=True, clamp=True)
    st.markdown("<h3 class='markdown-text', style='text-align: center'>Food Selection</h3>", unsafe_allow_html=True)

col21, col22 = st.columns(2)  # Colonne 1 plus large que colonne 2
with col21:
    # Centrer l'image avec un style CSS
    st.markdown("""
        <div style="text-align: center;">
            <img src="images/about.png" style="width: 50%; max-width: 300px; height: auto;" />
        </div>
    """, unsafe_allow_html=True)

with col22:
    st.markdown("<h2 class='markdown-text'>About PlateMate</h2>", unsafe_allow_html=True)
    st.markdown("""
    <span class='markdown-text'>
    The goal of PlateMate is to simplify daily meal management by providing 
    a visual, easy-to-use meal planner for healthy eating, along with precise 
    calculations of calories for each meal.
    Users will be able to filter recipes according to their dietary preferences 
    and health concerns, including vegetarian, low-carb, and gluten-free options. 
    PlateMate provides a wide selection of nutritious, balanced recipes that 
    cater to all kinds of dietary requirements.
    </span>
    """, unsafe_allow_html=True)



# Fermer la div principale
st.markdown('</div>', unsafe_allow_html=True)
