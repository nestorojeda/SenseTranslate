# SenseTranslate
SenseTranslate is a powerful translation tool that leverages advanced AI to provide summarization, sentiment analysis, and translation from Spanish to English.

## Project Overview

This project includes tools to process text documents through multiple AI pipelines:
- Text summarization using mT5_multilingual_XLSum
- Sentiment analysis using distilbert-base-multilingual-cased
- Translation from Spanish to English using opus-mt-es-en

## Directory Structure

- `code/`: Contains implementation code
    - `ui.py`: Streamlit user interface for the application
- `data/`: Contains test data
    - `short_phrases.csv`: Collection of short Spanish phrases
    - `long_phrases.csv`: Collection of longer Spanish text samples
- `docs/`: Contains sample text documents on various scientific topics
    - Multiple `.txt` files with Spanish content about physics, mathematics, etc.
- `notebooks/`: Contains Jupyter notebooks for prototyping
    - `1_summarize.ipynb`: Text summarization implementation
    - `2_sentiment.ipynb`: Sentiment analysis implementation
    - `3_translate.ipynb`: Translation implementation
    - `4_final.ipynb`: Combined implementation of all services

## Getting Started

To run this project, install the dependencies:

```bash
pip install -r requirements.txt
streamlit run ./code/ui.py
```
Then, open your web browser and navigate to `http://localhost:8501` to access the application.

## Usage
1. Upload a text document in Spanish.
2. The application will process the document and provide:
   - A summary of the text
   - Sentiment analysis results
   - Translated text in English

## License

This project is licensed under the MIT License - see the LICENSE file for details.