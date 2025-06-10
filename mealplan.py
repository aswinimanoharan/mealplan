import streamlit as st
import google.generativeai as genai

# 🎯 Set Gemini API key here
genai.configure(api_key="AIzaSyDSOBFmasJ4a_wX4Pu91bO5W4WhO1tFaHI")  # Replace with your key

# 🔮 Load Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# 🌈 Page Configuration
st.set_page_config(page_title="🍽️ Meal Plan Generator", layout="wide")

# 🧁 Stylish Header
st.markdown("""
    <h1 style='text-align: center; color: #ff6f61; font-family: Arial;'>🥗 Meal Plan Generator</h1>
    <h4 style='text-align: center; color: #4a4a4a;'>Personalized meal plans, recipes & shopping list powered by Gemini ✨</h4>
    <hr style='border: 1px solid #ff6f61;'/>
""", unsafe_allow_html=True)

# 🚀 Input Form
with st.form("meal_form"):
    st.markdown("### 🍴 Tell us about your preferences:")
    diet = st.selectbox("🌿 Dietary Preference", ["Vegan", "Vegetarian", "Keto", "Paleo", "Balanced", "Low Carb"])
    goal = st.selectbox("🎯 Health Goal", ["Weight Loss", "Muscle Gain", "Maintenance", "Energy Boost"])
    allergies = st.text_input("⚠️ Any allergies or dislikes?", placeholder="e.g. peanuts, dairy")
    submit = st.form_submit_button("Generate Meal Plan 🚀")

# 📋 Function to call Gemini
def generate_meal_plan(diet, goal, allergies):
    prompt = f"""
    Create a weekly meal plan for a user with the following:
    - Dietary preference: {diet}
    - Health goal: {goal}
    - Allergies/dislikes: {allergies}
    
    Include:
    - 🗓️ 7-day plan (Breakfast, Lunch, Dinner)
    - 🍲 Simple recipes for each meal
    - 🛒 Combined shopping list
    
    Format neatly with sections and emojis.
    """
    response = model.generate_content(prompt)
    return response.text

# 📦 Output Section
if submit:
    with st.spinner("Generating your delicious plan with Gemini... 🍳"):
        result = generate_meal_plan(diet, goal, allergies)
        st.markdown("## 📅 Your Weekly Meal Plan")
        st.markdown(result)

# 🎨 CSS Customization
st.markdown("""
<style>
body {
    font-family: 'Arial', sans-serif;
}
div.stButton > button {
    background-color: #ff6f61;
    color: white;
    border-radius: 10px;
    padding: 0.75em 1.5em;
    font-size: 18px;
}
div.stButton > button:hover {
    background-color: #ff3d3d;
}
</style>
""", unsafe_allow_html=True)
