# app/rag.py

import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.embeddings import get_embedding
from config import Config

# Novo cliente OpenAI com a nova API
client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)

def split_text(text, max_tokens=500):
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

def answer_question(context_text, question, model="gpt-4o"):
    try:
        chunks = split_text(context_text)
        if not chunks:
            return "Documento vazio ou sem conteúdo processável."

        embeddings = [get_embedding(chunk) for chunk in chunks]
        q_emb = get_embedding(question)

        similarities = cosine_similarity([q_emb], embeddings)[0]
        top_idx = int(np.argmax(similarities))
        retrieved = chunks[top_idx]

        prompt = f"""
Você é um assistente jurídico. Responda à pergunta com base no seguinte trecho.

Contexto:
\"\"\"{retrieved}\"\"\"

Pergunta:
{question}

Resposta:
"""

        # ✅ NOVA API
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"
