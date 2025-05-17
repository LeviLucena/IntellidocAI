# app/routes.py
from flask import Blueprint, request, jsonify
from .rag_engine import answer_question

bp = Blueprint('main', __name__)

@bp.route('/api/ask', methods=['POST'])
def api_ask():
    data = request.json
    question = data.get('question')
    context = data.get('context')
    if not question or not context:
        return jsonify({'error': 'Faltando question ou context'}), 400
    answer = answer_question(context, question)
    return jsonify({'answer': answer})
