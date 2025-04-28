from flask import request, jsonify, Response, stream_with_context
from . import ollamaClient
from . import app

@app.route('/optimize', methods=['POST'])
def optimize_prompt():
    if not request.is_json:
        return jsonify({'Error': "Content-Type must be application/json"}), 400
    
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"Error": "No prompt provided"}), 400

    def generate(prompt):
        for msg in ollamaClient.streamOllamaResponse(prompt):
            yield msg
    
    try:
        return Response(stream_with_context(generate(prompt)))
    except Exception as e:
        return jsonify({"Error": f"Server Error: {str(e)}"}, content_type='application/json')