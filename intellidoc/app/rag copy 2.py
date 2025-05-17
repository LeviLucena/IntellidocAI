# app/rag.py

import openai
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.embeddings import get_embedding
from config import Config  # <-- Importa a chave da config

# Carrega chave da API do ambiente
openai.api_key = Config.OPENAI_API_KEY  # Defina via variável de ambiente para segurança

def split_text(text, max_tokens=500):
    """
    Divide o texto em trechos (chunks) com limite de tamanho.
    """
    paragraphs = text.split('\n')
    chunks, chunk = [], ""
    for para in paragraphs:
        if len(chunk) + len(para) <= max_tokens:
            chunk += para + "\n"
        else:
            chunks.append(chunk.strip())
            chunk = para + "\n"
    if chunk:
        chunks.append(chunk.strip())
    return chunks

def answer_question(context_text, question):
    """
    Retorna resposta baseada no trecho mais relevante do documento, usando embeddings + OpenAI.
    """
    try:
        chunks = split_text(context_text)
        if not chunks:
            return "Documento vazio ou sem conteúdo processável."

        # Gera embeddings para contexto e pergunta
        embeddings = [get_embedding(chunk) for chunk in chunks]
        q_emb = get_embedding(question)

        # Calcula similaridade e encontra o trecho mais relevante
        similarities = cosine_similarity([q_emb], embeddings)[0]
        top_idx = int(np.argmax(similarities))
        retrieved = chunks[top_idx]

        # Prompt para o modelo
        prompt = f"""
Você é um assistente jurídico. Responda a pergunta com base no trecho a seguir.

Contexto:
\"\"\"{retrieved}\"\"\"

Pergunta:
{question}

Resposta:
"""

        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # ou gpt-4o-mini "gpt-3.5-turbo" se preferir
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=500
        )
        return completion.choices[0].message["content"].strip()
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"
