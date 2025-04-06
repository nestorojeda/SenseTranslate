import streamlit as st
from transformers import pipeline

# Uso: 
# 1. Instalar las dependencias necesarias:
#   pip install -r requirements.txt
# 2. Ejecutar la aplicación Streamlit:
#   streamlit run ui.py

# Constantes para emojis y otros iconos utilizados en la interfaz
EMOJI_POSITIVE = "😃"
EMOJI_NEGATIVE = "😔"
EMOJI_NEUTRAL = "😐"
EMOJI_TEXT_ORIGINAL = "📝"
EMOJI_TEXT_TRANSLATED = "🌐"
EMOJI_SENTIMENT = "😊"
EMOJI_SUMMARY = "📋"

# Configuración de la página de Streamlit con tema oscuro
st.set_page_config(page_title="SenseTranslate", page_icon=EMOJI_TEXT_TRANSLATED, layout="wide", initial_sidebar_state="expanded", 
                  menu_items=None)

# Aplicar tema oscuro con CSS personalizado
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
</style>
""", unsafe_allow_html=True)

# Inicialización de los modelos de IA para las diferentes tareas
summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")  # Modelo para resumir textos
sentiment_classifier = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")  # Modelo para análisis de sentimiento
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")  # Modelo para traducción español-inglés

# Título principal de la aplicación
st.title("SenseTranslate")

# Componente para subir archivos de texto
file_name = st.file_uploader("Sube archivo de texto (en castellano)", type=["txt"])

# Procesamiento del archivo cuando se ha cargado uno
if file_name is not None:
    # Lectura y decodificación del contenido del archivo
    text = file_name.getvalue().decode('utf-8')
    
    # Visualización del texto original con formato mejorado
    st.subheader(f"{EMOJI_TEXT_ORIGINAL} Texto Original")
    with st.container():
        st.markdown(f"""<div style="border:1px solid #444; border-radius:5px; padding:10px; background-color:#1a1a1a; color:#ddd">
                    {text}</div>""", unsafe_allow_html=True)
    
    # Sección de traducción con interfaz mejorada
    st.subheader(f"{EMOJI_TEXT_TRANSLATED} Texto Traducido")
    with st.spinner("Traduciendo..."):  # Muestra un spinner mientras se procesa
        if text.strip():  # Verifica que el texto no esté vacío
            # Realiza la traducción del texto
            translated_text = translator(text, max_length=512)
            with st.container():
                st.markdown(f"""<div style="border:1px solid #444; border-radius:5px; padding:10px; background-color:#192841; color:#ddd">
                            {translated_text[0]['translation_text']}</div>""", unsafe_allow_html=True)
    
    # Creación de dos columnas para mostrar el análisis de sentimiento y el resumen
    col1, col2 = st.columns(2)
    
    # Columna izquierda: Análisis de sentimiento
    with col1:
        st.subheader(f"{EMOJI_SENTIMENT} Análisis de Sentimiento")
        with st.spinner("Analizando sentimiento..."):
            if text.strip():
                # Procesa el texto para determinar el sentimiento
                sentiment = sentiment_classifier(text)
                label = sentiment[0]['label']
                # Estilos personalizados según el sentimiento detectado
                colors = {"positive": "#1e5631", "negative": "#8b2635", "neutral": "#4a505a"}
                emoji = {"positive": EMOJI_POSITIVE, "negative": EMOJI_NEGATIVE, "neutral": EMOJI_NEUTRAL}
                sentiment_labels = {"positive": "Positivo", "negative": "Negativo", "neutral": "Neutral"}
                display_label = sentiment_labels.get(label.lower(), label)
                # Muestra el resultado con un estilo visual acorde al sentimiento
                st.markdown(f"""<div style="text-align:center; padding:15px; border-radius:5px; 
                            background-color:{colors.get(label.lower(), '#2d3748')}; color:#f0f0f0; font-weight:bold">
                            {emoji.get(label.lower(), '')} {display_label}</div>""", unsafe_allow_html=True)
    
    # Columna derecha: Generación del resumen
    with col2:
        st.subheader(f"{EMOJI_SUMMARY} Resumen")
        with st.spinner("Resumiendo..."):
            if text.strip():
                # Genera un resumen del texto original
                summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
                # Muestra el resumen con formato mejorado
                st.markdown(f"""<div style="border:1px solid #444; border-radius:5px; padding:10px; 
                            background-color:#212121; color:#ddd">{summary[0]['summary_text']}</div>""", 
                            unsafe_allow_html=True)
