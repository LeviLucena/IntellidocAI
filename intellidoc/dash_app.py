import dash
from dash import html, dcc, Input, Output, State
import base64
import io

from app.ocr import extract_text_from_pdf
from app.rag import answer_question
from app.yolo_detector import (
    detect_visual_elements,
    detect_signatures_in_pdf,
    detect_and_draw_combined  # IMPORT CORRETO
)

external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(className="container mt-4", children=[
    html.Div([
        html.Img(src="/assets/logo.png", style={"height": "200px", "width": "auto"}, className="d-block mx-auto mb-4"),
    ], className="d-flex align-items-center mb-4"),

    dcc.Upload(
        id='upload-doc',
        children=html.Button([html.I(className="fas fa-upload mr-2"), "Upload PDF"], className="btn btn-primary"),
        multiple=False,
        className="mb-3"
    ),

    html.Div(id='file-name', className="mb-3 font-italic"),

    dcc.Checklist(
        id='yolo-check',
        options=[
            {'label': ' Rodar análise visual com YOLO', 'value': 'run_yolo'},
            {'label': ' Detectar assinaturas no documento', 'value': 'run_signatures'}
        ],
        value=[],
        className="form-check mb-3"
    ),

    dcc.Textarea(
        id='doc-content',
        style={'width': '100%', 'height': 200},
        className="form-control mb-3",
        placeholder="Conteúdo extraído do documento aparecerá aqui..."
    ),

    dcc.Input(
        id='question',
        type='text',
        placeholder='Pergunte algo...',
        className="form-control mb-3"
    ),

    html.Button(
        [html.I(className="fas fa-question-circle mr-2"), "Responder"],
        id='submit-question',
        className="btn btn-success mb-4"
    ),

    html.Div(id='answer-output', className="mb-4"),

    html.Hr(),

    html.H4("Resultados da Análise Visual", className="mb-3"),

    html.Pre(id='yolo-output', style={'backgroundColor': '#f9f9f9', 'padding': '10px'}, className="mb-4"),

    html.H4("Visualização das Detecções", className="mb-3"),

    html.Div(id='yolo-images')
])

@app.callback(
    Output('doc-content', 'value'),
    Output('file-name', 'children'),
    Output('yolo-output', 'children'),
    Output('yolo-images', 'children'),
    Input('upload-doc', 'contents'),
    State('upload-doc', 'filename'),
    State('yolo-check', 'value')
)
def handle_upload(contents, filename, yolo_opt):
    try:
        if contents:
            content_type, content_string = contents.split(',')
            decoded = base64.b64decode(content_string)
            file_stream = io.BytesIO(decoded)

            text = extract_text_from_pdf(file_stream)

            file_stream.seek(0)

            yolo_output = ""
            yolo_images = []

            if 'run_yolo' in yolo_opt or 'run_signatures' in yolo_opt:
                file_stream.seek(0)
                detections_objects = detect_visual_elements(file_stream)

                file_stream.seek(0)
                signature_detections = detect_signatures_in_pdf(file_stream)

                # Texto de saída
                flat_obj = [
                    f"[YOLOv8] Página {d['page']} - {d['label']} ({d['confidence']:.2f}): {d['bbox']}"
                    for page in detections_objects for d in page
                ]
                flat_sig = [
                    f"[ASSINATURA] Página {d['page']} - {d['label']} ({d['confidence']:.2f}): {d['bbox']}"
                    for d in signature_detections
                ]
                yolo_output += "\n".join(flat_obj + flat_sig) + "\n\n" if flat_obj or flat_sig else "Nenhuma detecção relevante.\n\n"

                # Imagem combinada
                file_stream.seek(0)
                combined_images = detect_and_draw_combined(file_stream)
                yolo_images = [
                    html.Div([
                        html.H6(f"Detecções - Página {i + 1}"),
                        html.Img(
                            src=f"data:image/png;base64,{img}",
                            style={'maxWidth': '100%', 'border': '1px solid #ccc', 'marginBottom': '20px'}
                        )
                    ])
                    for i, img in enumerate(combined_images)
                ]

            return text, filename, yolo_output, yolo_images

        return "", "", "", []

    except Exception as e:
        return f"Erro no processamento: {str(e)}", "", "", []

@app.callback(
    Output('answer-output', 'children'),
    Input('submit-question', 'n_clicks'),
    State('doc-content', 'value'),
    State('question', 'value')
)
def generate_answer(n_clicks, context_text, question):
    if n_clicks and question:
        return answer_question(context_text, question)
    return ""

if __name__ == '__main__':
    app.run(debug=True)
