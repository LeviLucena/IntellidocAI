# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_super_forte'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or 'sua api aqui'

    # Outros parâmetros configuráveis
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    ALLOWED_EXTENSIONS = {'pdf'}

    # Configurações de modelo / RAG
    EMBEDDING_DIM = 1536  # por exemplo, OpenAI embeddings
