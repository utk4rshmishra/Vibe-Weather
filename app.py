import streamlit as st
import requests
from groq import Groq

# --- UI HACKS & PAGE SETUP ---
st.set_page_config(page_title="Vibe-Check Weather", page_icon="🌤️", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
    .stApp { background: linear-gradient(135deg, #1e130c, #9a8478); color: white; }
    .vibe-box { background-color: rgba(255, 255, 255, 0.1); border-radius: 15px; padding: 20px; border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(10px); margin-bottom: 20px;}
    div.stButton > button { background-color: #FF7E5F; color: white; border-radius: 8px; border: none; padding: 10px 24px; font-weight: bold; width: 100%; transition: 0.3s; }
    div.stButton > button:hover { background-color: #FEB47B; transform: scale(1.02); }
</style>
""", unsafe_allow_html=True)

st.title("🌤️ The Vibe-Check Weather")
st.write("Enter a city to get the real forecast. Not just numbers, but *vibes*.")

# --- THE INPUT ---
city = st.text_input("📍 Where are you right now?", placeholder="e.g., London, Tokyo, New York")

if st.button("Check the Vibe 🚀"):
    if city:
        with st.spinner("Looking at the sky..."):
            try:
                # 1. GET WEATHER DATA
                weather_api = st.secrets["OPENWEATHER_API_KEY"]
                weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=imperial"
                weather_data = requests.get(weather_url).json()

                # Check if city is found
                if weather_data.get("cod") != 200:
                    st.error("City not found! Check your spelling.")
                else:
                    # Extract the boring numbers
                    temp = round(weather_data["main"]["temp"])
                    desc = weather_data["weather"][0]["description"]
                    humidity = weather_data["main"]["humidity"]

                    # 2. ASK THE AI FOR THE VIBE
                    groq_api = st.secrets["GROQ_API_KEY"]
                    client = Groq(api_key=groq_api)
                    
                    prompt = f"""
                    The current weather in {city} is {temp}°F and {desc}. Humidity is {humidity}%.
                    You are a sassy, highly opinionated, modern AI meteorologist. 
                    Reply in exactly this format with NO extra text:
                    
                    VIBE CHECK: [2 short, hilarious sentences about what this weather means for my life]
                    OUTFIT: [1 sentence funny outfit recommendation]
                    TOUCH GRASS INDEX: [A number from 1 to 100] - [1 short reason why]
                    """
                    
                    response = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama-3.1-8b-instant",
                    )
                    
                    ai_text = response.choices[0].message.content

                    # 3. DISPLAY THE BEAUTIFUL DASHBOARD
                    st.markdown("### 📡 Live Atmospheric Data")
                    
                    # Create 3 columns for the standard metrics
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Temperature", f"{temp}°F")
                    col2.metric("Condition", desc.title())
                    col3.metric("Humidity", f"{humidity}%")

                    # Display the AI's sassy interpretation inside our custom CSS box
                    st.markdown(f'<div class="vibe-box">{ai_text}</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Whoops! Something broke: {e}")
    else:
        st.warning("Please type a city first!")
