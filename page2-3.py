import streamlit as st

# Activer la mise en page large
st.set_page_config(layout="wide")

# Définir un style personnalisé
custom_style = """
    <style>
    .custom-style {
        background-color: #386641;
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
        text-align: center;
    }
    .custom-style img {
        max-width: 100%;
        height: auto;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
"""

# Injecter le style CSS dans la page
st.markdown(custom_style, unsafe_allow_html=True)

# Section Table of Contents stylisée
st.markdown("""
    <div class='custom-style'>
        <h2>Table of Contents</h2>
        <div style='display: flex; justify-content: space-around;'>
            <div>
                <img src='images/recipes.png' alt='Recipes'>
                <h3>Recipes</h3>
            </div>
            <div>
                <img src='images/mealPlan.png' alt='Meal Planning'>
                <h3>Meal Planning</h3>
            </div>
            <div>
                <img src='images/food.png' alt='Food Selection'>
                <h3>Food Selection</h3>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Section About stylisée
st.markdown("""
    <div class='custom-style'>
        <h2>About PlateMate</h2>
        <p>The goal of PlateMate is to simplify daily meal management by providing 
        a visual, easy-to-use meal planner for healthy eating, along with precise 
        calculations of calories for each meal.</p>
        <p>Users will be able to filter recipes according to their dietary preferences 
        and health concerns, including vegetarian, low-carb, and gluten-free options. 
        PlateMate provides a wide selection of nutritious, balanced recipes that 
        cater to all kinds of dietary requirements.</p>
    </div>
    """, unsafe_allow_html=True)
