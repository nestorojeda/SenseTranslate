import streamlit as st
from transformers import pipeline
from PIL import Image
import threading
from functools import partial

# Constants
EMOJI_POSITIVE = "😃"
EMOJI_NEGATIVE = "😔"
EMOJI_NEUTRAL = "😐"
EMOJI_TEXT_ORIGINAL = "📝"
EMOJI_TEXT_TRANSLATED = "🌐"
EMOJI_SENTIMENT = "😊"
EMOJI_SUMMARY = "📋"

# Force dark theme
st.set_page_config(page_title="SenseTranslate", page_icon=EMOJI_TEXT_TRANSLATED, layout="wide", initial_sidebar_state="expanded", 
                  menu_items=None)

# Apply dark theme with custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
</style>
""", unsafe_allow_html=True)

# Create a function to load a pipeline with spinner
def load_pipeline_with_spinner(pipeline_type, model_name):
    with st.spinner(f"Loading {pipeline_type} model..."):
        return pipeline(pipeline_type, model=model_name)

# Initialize placeholders
summarizer = None
sentiment_classifier = None
translator = None

# Create and start threads for loading models
thread1 = threading.Thread(
    target=partial(lambda: globals().__setitem__('summarizer', 
                                                load_pipeline_with_spinner("summarization", "csebuetnlp/mT5_multilingual_XLSum")))
)
thread2 = threading.Thread(
    target=partial(lambda: globals().__setitem__('sentiment_classifier', 
                                               load_pipeline_with_spinner("text-classification", "lxyuan/distilbert-base-multilingual-cased-sentiments-student")))
)
thread3 = threading.Thread(
    target=partial(lambda: globals().__setitem__('translator', 
                                               load_pipeline_with_spinner("translation", "Helsinki-NLP/opus-mt-es-en")))
)

# Start all threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to complete
thread1.join()
thread2.join()
thread3.join()

st.title("SenseTranslate")

file_name = st.file_uploader("Sube archivo de texto (en castellano)", type=["txt"])

if file_name is not None:
    text = file_name.getvalue().decode('utf-8')
    
    # Display original text in a bordered container
    st.subheader(f"{EMOJI_TEXT_ORIGINAL} Texto Original")
    with st.container():
        st.markdown(f"""<div style="border:1px solid #444; border-radius:5px; padding:10px; background-color:#1a1a1a; color:#ddd">
                    {text}</div>""", unsafe_allow_html=True)
    
    # Translation section with improved UI
    st.subheader(f"{EMOJI_TEXT_TRANSLATED} Texto Traducido")
    with st.spinner("Traduciendo..."):
        if text.strip():
            translated_text = translator(text, max_length=512)
            with st.container():
                st.markdown(f"""<div style="border:1px solid #444; border-radius:5px; padding:10px; background-color:#192841; color:#ddd">
                            {translated_text[0]['translation_text']}</div>""", unsafe_allow_html=True)
    
    # Create two columns for sentiment and summary
    col1, col2 = st.columns(2)
    
    # Sentiment analysis in first column
    with col1:
        st.subheader(f"{EMOJI_SENTIMENT} Análisis de Sentimiento")
        with st.spinner("Analizando sentimiento..."):
            if text.strip():
                sentiment = sentiment_classifier(text)
                label = sentiment[0]['label']
                # Style based on sentiment - adjusted for dark mode
                colors = {"positive": "#1e5631", "negative": "#8b2635", "neutral": "#4a505a"}
                emoji = {"positive": EMOJI_POSITIVE, "negative": EMOJI_NEGATIVE, "neutral": EMOJI_NEUTRAL}
                sentiment_labels = {"positive": "Positivo", "negative": "Negativo", "neutral": "Neutral"}
                display_label = sentiment_labels.get(label.lower(), label)
                st.markdown(f"""<div style="text-align:center; padding:15px; border-radius:5px; 
                            background-color:{colors.get(label.lower(), '#2d3748')}; color:#f0f0f0; font-weight:bold">
                            {emoji.get(label.lower(), '')} {display_label}</div>""", unsafe_allow_html=True)
    
    # Summarization in second column
    with col2:
        st.subheader(f"{EMOJI_SUMMARY} Resumen")
        with st.spinner("Resumiendo..."):
            if text.strip():
                summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
                st.markdown(f"""<div style="border:1px solid #444; border-radius:5px; padding:10px; 
                            background-color:#212121; color:#ddd">{summary[0]['summary_text']}</div>""", 
                            unsafe_allow_html=True)
