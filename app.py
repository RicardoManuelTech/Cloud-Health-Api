from flask import Flask, jsonify
import platform
import datetime

app = Flask(__name__)

APP_NAME = "Cloud Health API"
VERSION = "1.0.0"


@app.route("/")
def home():
    return jsonify({
        "application": APP_NAME,
        "status": "running",
        "version": VERSION
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    })


@app.route("/metrics")
def metrics():
    return jsonify({
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "platform_release": platform.release()
    })


@app.route("/version")
def version():
    return jsonify({
        "application": APP_NAME,
        "version": VERSION
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
