# PlateMate   

## Keywords   
API, Nutrition, Recipes, Calories, Meal Planning, Food, Streamlit   

## 1. Overview
PlateMate is a user-friendly meal planning app focused on nutrition. It provides a wide selection of recipes based on dietary preferences and calorie needs. The app helps users:    
- Find 6 recipes tailored to your diet and calorie range.
- Discover recipes based on specific ingredients.
- Create weekly meal plans that align with your diet.

## 2. Technologies
- Spoonacular API: Provides recipe data, including nutritional info, ingredients, and meal plans.   
- Streamlit: Used for building and deploying the app.    

## 3. Features

### A. Recipe Search by Diet & Calories
Filter recipes based on diet (e.g., Gluten-Free) and calorie range using /recipes/complexSearch and get detailed information using /recipes/{id}/information.   

### B. Meal Planning
Generate a weekly meal plan based on diet using /mealplanner/generate, with recipes for breakfast, lunch, and dinner.   

### C. Ingredient-Based Recipes
Find recipes based on available ingredients using /recipes/findByIngredients.   

## 4. Deployment
PlateMate is built with Streamlit, making deployment simple and fast.   
Make sure to enable dark mode in Streamlit for the best visual experience of the site.    
[PlateMate](https://platematedatacamp.streamlit.app/)
