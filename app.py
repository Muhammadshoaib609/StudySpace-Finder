import streamlit as st
import pandas as pd
from location_helper import filter_spaces

st.set_page_config(page_title="StudySpace Finder", layout="wide")

st.title("📚 StudySpace Finder & Peer Circle")
st.write("Find quiet study spots and study circles within your range!")

# Sidebar Filters
st.sidebar.header("📍 Location & Preferences")

# Mock user location (Islamabad coordinates default)
user_lat = st.sidebar.number_input("Your Latitude", value=33.6844, format="%.4f")
user_lon = st.sidebar.number_input("Your Longitude", value=73.0479, format="%.4f")

# Range Slider
radius_km = st.sidebar.slider("Select Search Radius (km)", min_value=1.0, max_value=15.0, value=5.0)

# Noise Filter
noise_pref = st.sidebar.selectbox("Preferred Noise Level", ["All", "Silent", "Moderate"])

# Filter Data
filtered_data = filter_spaces("study_spaces.csv", user_lat, user_lon, radius_km, noise_pref)

# Display Results
st.subheader(f"Results within {radius_km} km radius")

if not filtered_data.empty:
    # Map Visualization
    st.map(filtered_data.rename(columns={'latitude': 'lat', 'longitude': 'lon'}))
    
    # Data Table
    st.dataframe(filtered_data[['name', 'category', 'noise_level', 'distance_km', 'has_wifi', 'rating']])
else:
    st.warning("No study spaces found within this range. Try increasing the search radius!")

# AI Study Roadmap Feature
st.markdown("---")
st.subheader("🤖 AI Study Companion & Plan")
user_topic = st.text_input("What subject or topic are you studying today?")

if st.button("Generate AI Study Plan"):
    if user_topic:
        st.info(f"Generating personalized study roadmap for **{user_topic}**...")
        # Placeholder for AI Response (Connect Gemini/Mistral API here)
        st.success(f"**AI Recommendation:** Break down '{user_topic}' into 25-min Pomodoro sessions. Focus on core concepts for the first hour at your selected Silent Space!")
    else:
        st.error("Please enter a topic first.")