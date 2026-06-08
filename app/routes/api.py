from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "enthrallverse-api"
    }), 200
