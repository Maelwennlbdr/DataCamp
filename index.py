import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="PlateMate", layout="wide")

def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Ajouter le style CSS
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

# Page d'accueil avec table of contents et about
st.markdown("<h1 style='text-align: center'>Bienvenue sur PlateMate</h1>", unsafe_allow_html=True)

# Table of contents
st.markdown("<h2 style='text-align: center'>Table of Contents</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("[Recipes](recipes.py)")

with col2:
    st.markdown("[Meal Planning](food_selection.py)")

with col3:
    st.markdown("[About PlateMate](#about)")

# Section About
st.markdown("<h2 id='about'>About PlateMate</h2>", unsafe_allow_html=True)
st.write("""
PlateMate est une application qui aide à gérer les repas quotidiens en fournissant des recettes saines,
des calculateurs de calories, et des filtres selon les régimes alimentaires.
""")
