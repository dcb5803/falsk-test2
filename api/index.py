# api/index.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded API key (replace with your own)
API_KEY = "MY_SECRET_KEY_123"

@app.before_request
def check_api_key():
    provided = request.headers.get("X-API-Key") or request.args.get("api_key")
    if provided != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!", "source": "Flask on Vercel"})

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ok": True, "path": "ping"})

# WSGI handler for Vercel
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
