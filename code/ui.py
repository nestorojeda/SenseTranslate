import streamlit as st
from transformers import pipeline
from PIL import Image

summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")
sentiment_classifier = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en") 

st.title("SenseTranslate")

file_name = st.file_uploader("Upload a txt file", type=["txt"])

if file_name is not None:
    text = file_name.getvalue().decode('utf-8')
    st.subheader("Original Text")
    st.write(text)

    st.subheader("Translated Text")
    with st.spinner("Translating..."):
        # Ensure the text is not empty
        if text.strip():
            # Perform translation
            translated_text = translator(text, max_length=512)
            # Display the translated text
            st.write(translated_text[0]['translation_text'])

    st.subheader("Sentiment Analysis")
    with st.spinner("Analyzing sentiment..."):
        # Ensure the text is not empty
        if text.strip():
            # Perform sentiment analysis
            sentiment = sentiment_classifier(text)
            st.write(sentiment[0]['label'])

    st.subheader("Summarization")
    with st.spinner("Summarizing..."):
        # Ensure the text is not empty
        if text.strip():
            # Perform summarization
            summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
            st.write(summary[0]['summary_text'])
