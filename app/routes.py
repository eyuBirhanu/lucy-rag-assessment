from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check to verify the API is running."""
    return jsonify({"status": "success", "message": "API is up and running!"}), 200

@main.route('/api/upload', methods=['POST'])
def upload_pdf():
    # TODO: Implement PDF upload and RAG ingestion
    return jsonify({"status": "success", "message": "Endpoint ready for PDF upload."}), 200

@main.route('/api/chat', methods=['POST'])
def chat():
    # TODO: Implement RAG retrieval and LLM chat
    return jsonify({"status": "success", "message": "Endpoint ready for chat."}), 200