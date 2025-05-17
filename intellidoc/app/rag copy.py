# app/rag.py
import openai
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from app.embeddings import get_embedding

openai.api_key = "SUA_CHAVE_OPENAI"

def split_text(text, max_tokens=500):
    paragraphs = text.split('\n')
    chunks, chunk = [], ""
    for para in paragraphs:
        if len(chunk) + len(para) <= max_tokens:
            chunk += para + "\n"
        else:
            chunks.append(chunk)
            chunk = para + "\n"
    if chunk:
        chunks.append(chunk)
    return chunks

def answer_question(context_text, question):
    chunks = split_text(context_text)
    embeddings = [get_embedding(chunk) for chunk in chunks]
    q_emb = get_embedding(question)

    similarities = cosine_similarity([q_emb], embeddings)[0]
    top_idx = int(np.argmax(similarities))
    retrieved = chunks[top_idx]

    # Gera resposta com contexto
    prompt = f"""
Você é um assistente jurídico. Responda a pergunta com base no trecho a seguir.

Contexto:
\"\"\"{retrieved}\"\"\"

Pergunta:
{question}

Resposta:
"""

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return completion.choices[0].message["content"]
