import streamlit as st
import google.generativeai as genai

# Set Gemini API Key
GEMINI_API_KEY = "AIzaSyCrhpUCh9SCIKWjSQEWKYamnuXDR0LvIIA"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# Apply new CSS styles (orange title, pink subheaders, white text)
st.markdown("""
    <style>
        body, .stApp {
            background-color: black;
            color: white;
        }
        h1 {
            color: orange !important;
            text-align: center;
        }
        h2, h3 {
            color: pink !important;
            text-align: center;
        }
        p, label {
            color: white !important;
        }
        .stTextInput, .stNumberInput, .stSelectbox {
            background-color: black !important;
            color: white !important;
        }
        .stButton > button {
            background-color: black !important;
            color: white !important;
            border: 2px solid white;
        }
        .stButton > button:active {
            background-color: red !important;
            color: white !important;
        }
        .center-text {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Center-align title and subtitles
st.markdown("<h1>Personalized Diet and Workout Recommender ☕</h1>", unsafe_allow_html=True)
st.markdown("<h2>Your Best Food and Exercise Advisor 🥄</h2>", unsafe_allow_html=True)

# Function to get recommendations from Gemini
def get_gemini_recommendations(data):
    prompt = (
        f"Diet Recommendation System:\n"
        f"Recommend 5 restaurant names, 5 breakfast items, 5 dinner items, and 5 workout routines based on:\n"
        f"Age: {data['age']}\n"
        f"Gender: {data['gender']}\n"
        f"Weight: {data['weight']} pounds\n"
        f"Height: {data['height_feet']} feet {data['height_inches']} inches\n"
        f"Veg_or_Nonveg: {data['veg_or_nonveg']}\n"
        f"Address: {data['address']}\n"
        f"Food Allergies: {data['allergies']}\n"
    )
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text if response else "No recommendations available."

# Input fields
age = st.number_input("Age", min_value=0)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.number_input("Weight (pounds)", min_value=0)

# Height input as feet and inches
height_feet = st.number_input("Height (feet)", min_value=0)
height_inches = st.number_input("Height (inches)", min_value=0, max_value=11)

veg_or_nonveg = st.selectbox("Veg or Non-Veg", ["Veg", "Non-Veg"])
address = st.text_input("Address")
allergies = st.text_input("Food allergies")

if st.button("Get Recommendations"):
    input_data = {
        'age': age,
        'gender': gender,
        'weight': weight,
        'height_feet': height_feet,
        'height_inches': height_inches,
        'veg_or_nonveg': veg_or_nonveg,
        'address': address,
        'allergies': allergies
    }
    
    results = get_gemini_recommendations(input_data)

    # Center-aligned recommendations header
    st.markdown("<h2>Recommendations</h2>", unsafe_allow_html=True)
    st.write(results)