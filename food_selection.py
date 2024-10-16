import streamlit as st

st.set_page_config(page_title="Food Selection", layout="wide")

# Interface Food Selection
st.title("Food Selection")

# Dictionnaire des aliments sélectionnés
selected_foods = {
    "Vegetables": [],
    "Proteins": [],
    "Grains": []
}

# Interface pour choisir des aliments
with st.expander("Select Vegetables"):
    vegetables = ["Carrot", "Broccoli", "Spinach"]
    selected_foods["Vegetables"] = [veg for veg in vegetables if st.checkbox(veg)]

with st.expander("Select Proteins"):
    proteins = ["Chicken", "Tofu", "Beef"]
    selected_foods["Proteins"] = [protein for protein in proteins if st.checkbox(protein)]

with st.expander("Select Grains"):
    grains = ["Rice", "Oats", "Quinoa"]
    selected_foods["Grains"] = [grain for grain in grains if st.checkbox(grain)]

# Afficher la sélection
st.write("Selected Foods:")
st.write(selected_foods)
