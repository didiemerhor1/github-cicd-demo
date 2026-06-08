from flask import Flask, jsonify
from routes.api import api

app = Flask(__name__)

# Register API blueprint
app.register_blueprint(api)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Enthrallverse"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
