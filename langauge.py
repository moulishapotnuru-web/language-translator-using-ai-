import streamlit as st
from googletrans import Translator
import base64

# Function to set background image
def add_bg(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        h1, h2, h3, h4, h5, h6, p, label {{
            color: white !important;
            font-weight: bold;
        }}
        
        </style>
        """,
        unsafe_allow_html=True
    )

# Call background function
add_bg("background.jpg")

# Page title
st.title("🌍 Simple Language Translator")

translator = Translator()

# Text input
text = st.text_area("Enter text to translate")

# Language selection
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-cn",
    "Japanese": "ja"
}

target_lang = st.selectbox("Select target language", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text:
        translated = translator.translate(text, dest=languages[target_lang])
        st.success("Translated Text:")
        st.write(translated.text)
    else:
        st.warning("Please enter some text.")