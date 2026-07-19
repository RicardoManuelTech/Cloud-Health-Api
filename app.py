from flask import Flask, jsonify
import platform
import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger(__name__)
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
    logger.info("GET /health request received")
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
    logger.info("GET /version request received")
    return jsonify({
        "application": APP_NAME,
        "version": VERSION
    })

@app.route("/error")
def error():
    raise Exception("Test exception")

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not Found",
        "message": "The requested resource does not exist."
    }), 404

@app.errorhandler(Exception)
def handle_exception(error):
    logger.exception("Unhandled exception")

    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred."
    }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
