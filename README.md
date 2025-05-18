<p align="center">

  <!-- Linguagem principal -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  </a>

  <!-- Frameworks Web -->
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask" />
  </a>
  <a href="https://dash.plotly.com/">
    <img src="https://img.shields.io/badge/-Dash-1E1E1E?style=flat-square&logo=plotly&logoColor=white" alt="Dash" />
  </a>

  <!-- IA / LLMs -->
  <a href="https://platform.openai.com/">
    <img src="https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI API" />
  </a>

  <!-- NLP e Vetorização -->
  <a href="https://scikit-learn.org/">
    <img src="https://img.shields.io/badge/-Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-learn" />
  </a>
  <a href="https://numpy.org/">
    <img src="https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy" />
  </a>
  <a href="https://github.com/facebookresearch/faiss">
    <img src="https://img.shields.io/badge/-FAISS-005571?style=flat-square&logo=facebook&logoColor=white" alt="FAISS" />
  </a>

  <!-- OCR e Visão Computacional -->
  <a href="https://pypi.org/project/pytesseract/">
    <img src="https://img.shields.io/badge/-Tesseract%20OCR-5A4FCF?style=flat-square&logo=tesseract&logoColor=white" alt="Tesseract OCR" />
  </a>
  <a href="https://pillow.readthedocs.io/">
    <img src="https://img.shields.io/badge/-Pillow-7A4F87?style=flat-square&logo=python&logoColor=white" alt="Pillow" />
  </a>
  <a href="https://github.com/ultralytics/ultralytics">
    <img src="https://img.shields.io/badge/-YOLOv8-00FFFF?style=flat-square&logo=github&logoColor=black" alt="YOLOv8 Ultralytics" />
  </a>
  <a href="https://opencv.org/">
    <img src="https://img.shields.io/badge/-OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV" />
  </a>

  <!-- Leitura de PDFs -->
  <a href="https://pymupdf.readthedocs.io/">
    <img src="https://img.shields.io/badge/-PyMuPDF-005F6A?style=flat-square&logo=readthedocs&logoColor=white" alt="PyMuPDF" />
  </a>

  <!-- Manipulação e Requests -->
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas" />
  </a>
  <a href="https://requests.readthedocs.io/">
    <img src="https://img.shields.io/badge/-Requests-20232A?style=flat-square&logo=python&logoColor=white" alt="Requests" />
  </a>

  <!-- Variáveis de Ambiente -->
  <a href="https://pypi.org/project/python-dotenv/">
    <img src="https://img.shields.io/badge/-Dotenv-ECD53F?style=flat-square&logo=python&logoColor=black" alt="Dotenv" />
  </a>

  <!-- Servidor de Produção -->
  <a href="https://gunicorn.org/">
    <img src="https://img.shields.io/badge/-Gunicorn-499848?style=flat-square&logo=linux&logoColor=white" alt="Gunicorn" />
  </a>

  <!-- Status do projeto -->
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square" alt="Status" />

  <!-- Licença -->
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT License" />

</p>

![image](https://github.com/user-attachments/assets/c14e3353-47cb-44d3-82f8-da2936298937)

# 🧠 IntelliDoc AI - Análise Inteligente de Documentos com OCR, RAG e Visão Computacional
**IntelliDoc AI** é um sistema web inteligente construído em Python que realiza **análise automatizada de documentos** em PDF, combinando técnicas de **OCR, RAG (Retrieval-Augmented Generation)** e **detecção visual com YOLOv8**. A interface web interativa é construída com **Dash** e roda sobre um backend **Flask**, integrando processamento de linguagem natural, visão computacional e modelos generativos.

---

## 🚀 Funcionalidades

- 📄 **Upload de documentos PDF**
- 🔍 **Extração de texto (OCR) com PyMuPDF e pytesseract**
- 🎯 **Detecção visual com YOLOv8 (Ultralytics + OpenCV)**
- ❓ **Perguntas e respostas com RAG + OpenAI (embeddings + LLM)**
- 🖼️ **Visualização de imagens com marcações dos objetos detectados**
- 🌐 Interface responsiva com Dash + Bootstrap

## 🧪 Exemplo de Uso
- Faça upload de um PDF (ex: contrato, fatura, laudo técnico).
- Extraia o texto com OCR automaticamente.
- Ative a opção “Rodar YOLO” para identificar elementos visuais (selos, logos, carimbos, assinaturas etc.).
- Digite uma pergunta sobre o conteúdo do documento.
- Veja a resposta gerada com base nos trechos mais relevantes.

https://github.com/user-attachments/assets/9228f762-07f9-482a-a931-d3042f04d5f5

---

## 🧰 Tecnologias Utilizadas

| Área                     | Ferramentas / Bibliotecas                                                  |
|--------------------------|----------------------------------------------------------------------------|
| **Interface Web**        | [Dash](https://dash.plotly.com/), [Flask](https://flask.palletsprojects.com/) |
| **OCR**                  | [PyMuPDF](https://pymupdf.readthedocs.io/), [pytesseract](https://github.com/madmaze/pytesseract), [Pillow](https://python-pillow.org/) |
| **Visão Computacional**  | [YOLOv8 (Ultralytics)](https://docs.ultralytics.com/), [OpenCV](https://opencv.org/) |
| **RAG & NLP**            | [OpenAI API](https://platform.openai.com/), [NumPy](https://numpy.org/), [scikit-learn](https://scikit-learn.org/), [faiss-cpu](https://github.com/facebookresearch/faiss) |
| **Ambiente e Servidor**  | [python-dotenv](https://pypi.org/project/python-dotenv/), [gunicorn](https://gunicorn.org/), [requests](https://requests.readthedocs.io/en/latest/) |
| **Outros**               | [pandas](https://pandas.pydata.org/) (opcional para relatórios futuros) |

## 🧠 Futuras Melhorias
- Armazenamento vetorial com FAISS + persistência
- Integração com banco de dados (PostgreSQL ou SQLite)
- Dashboard de relatórios com pandas + Plotly
- Suporte a múltiplos arquivos e histórico de perguntas
- Deploy no Hugging Face Spaces ou AWS/GCP

---

## 📁 Estrutura do Projeto
```bash
intellidoc/
├── __pycache__/                     # Cache interno do Python (pode ser ignorado ou excluído do controle de versão)
├── app/                             # Lógica de backend e processamento inteligente
│   ├── __pycache__/                 # Cache dos módulos Python (pode ser ignorado)
│   ├── __init__.py                  # Inicializador do pacote app
│   ├── routes.py                    # (Opcional) Se estiver usando Flask ou fastAPI para rotas customizadas
│   ├── ocr.py                       # Extração de texto com PyMuPDF + Tesseract OCR
│   ├── yolo_detector.py            # Detecção visual com YOLO (objetos e assinaturas)
│   ├── rag.py                       # Retrieval-Augmented Generation (RAG) com OpenAI
│   ├── embeddings.py                # Criação de embeddings e integração com vector store
│   ├── vector_store.py              # Faiss index e recuperação vetorial de documentos
│   ├── nlp_utils.py                 # Utilitários de NLP, tokenização, limpeza etc.
├── assets/
│   ├── logo.png                     # Logotipo exibido no layout do Dash
├── models/signatures/              # Diretório de treino YOLO para assinaturas
│   ├── datasets/
│   │   ├── train/                   # Conjunto de treino (imagens + labels YOLO)
│   │   ├── valid/                   # Conjunto de validação (imagens + labels YOLO)
│   │   ├── data.yaml                # Arquivo de configuração para o treinamento
│   │   ├── signature.yaml           # Configuração específica do dataset de assinaturas
│   ├── runs/detect/
│   │   ├── train1 ... train7/       # Experimentos de treino (YOLOv8) com pesos, logs etc.
│   │   │   ├── weights/
│   │   │   │   ├── best.pt          # Melhor modelo (assinaturas) salvo durante o treino
│   │   │   │   ├── last.pt          # Último estado salvo do modelo
│   ├── train_signatures.py         # Script de treino para assinatura com Ultralytics YOLO
│   ├── yolov8n.pt                   # Modelo pré-treinado geral (objetos) da Ultralytics
├── templates/                       # (Opcional) Para templates HTML, se usar Flask (não usado por Dash diretamente)
├── dash_app.py                      # Interface principal Dash com uploads, visualização, OCR, RAG e YOLO
├── config.py                        # Leitura de variáveis de ambiente, chaves da OpenAI, caminhos de modelo, etc.
├── requirements.txt                 # Lista atualizada de dependências do projeto
├── run.py                           # Entry point para execução local ou produção (via gunicorn, por exemplo)
├── yolov8n.pt                       # Cópia local (redundante?) do modelo pré-treinado YOLO para objetos

```

## 🛠️ Como Executar o Projeto Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/LeviLucena/IntellidocAI.git
cd intellidoc
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Crie um arquivo .env na raiz com o seguinte conteúdo:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Execute o app (modo desenvolvimento)

```bash
python run.py
```

Acesse o app em: http://localhost:8050

### 6. Executar em produção (via gunicorn)

```bash
gunicorn run:server
```

## 📚 Referências

- OpenAI Python SDK (v1.x): https://github.com/openai/openai-python
- YOLOv8 by Ultralytics: https://docs.ultralytics.com/
- Dash Docs: https://dash.plotly.com/
- pytesseract OCR: https://github.com/madmaze/pytesseract
- PyMuPDF: https://pymupdf.readthedocs.io/
- scikit-learn (cosine_similarity): https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html
- FAISS Search: https://github.com/facebookresearch/faiss
- RAG Paper: https://arxiv.org/abs/2005.11401

- ## 🤝 Como Contribuir
Sinta-se à vontade para contribuir, sugerir melhorias ou relatar problemas para ajudar a desenvolver este projeto.

## 📄 Licença
Este projeto está licenciado sob a licença MIT — veja [LICENSE](https://github.com/github/gitignore/blob/main/LICENSE) para detalhes.
