# app/nlp_utils.py
import re

def clean_text(text):
    """
    Limpa e normaliza texto para NLP.
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()
