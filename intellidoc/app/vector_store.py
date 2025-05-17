# app/vector_store.py
import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embedding, text):
        """
        Adiciona embedding e texto ao índice.
        """
        self.index.add(np.array([embedding], dtype='float32'))
        self.texts.append(text)

    def search(self, query_embedding, k=5):
        """
        Busca os k textos mais similares ao embedding da query.
        """
        D, I = self.index.search(np.array([query_embedding], dtype='float32'), k)
        results = [self.texts[i] for i in I[0] if i != -1]
        return results
