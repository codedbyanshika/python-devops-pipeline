from flask import Flask, jsonify
from datetime import datetime, timezone
import socket

app = Flask(__name__)


# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Python DevOps Pipeline!",
        "status": "Application is running"
    })


# Application information API
@app.route("/api/v1/info")
def info():
    return jsonify({
        "application": "Python DevOps Application",
        "hostname": socket.gethostname(),
        "current_time": datetime.now(timezone.utc).isoformat(),
        "status": "Running"
    })


# Health check API
@app.route("/api/v1/healthz")
def health():
    return jsonify({
        "status": "Healthy",
        "message": "Application is working properly"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)