# app/embeddings.py
import openai
import numpy as np
from config import Config

# Inicializa o cliente OpenAI com a nova API
client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)

def get_embedding(text: str, model: str = "text-embedding-3-small") -> np.ndarray:
    """
    Gera o embedding de um texto usando o modelo especificado da OpenAI.
    
    Args:
        text (str): Texto para gerar embedding.
        model (str): Modelo de embedding (padrão: "text-embedding-3-small").
    
    Returns:
        np.ndarray: Vetor de embedding do texto.
    """
    try:
        text = text.replace("\n", " ")
        response = client.embeddings.create(
            input=[text],
            model=model
        )
        return np.array(response.data[0].embedding)
    except Exception as e:
        print(f"[Embedding Error] {str(e)}")
        # Retorna vetor nulo de dimensão padrão (1536 para text-embedding-3-small)
        return np.zeros(1536)
