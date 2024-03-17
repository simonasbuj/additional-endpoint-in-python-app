from flask import Flask, jsonify
from waitress import serve
import random

from service.service import Service

app = Flask(__name__)

@app.route('/health')
def health():
    app.logger.info('Health check requested')
    return jsonify(status="OK")

@app.route('/run-service')
def run_service():
    correlation_id = f"correlation-id-api-request-{random.randint(1, 999999)}"
    s = Service(correlation_id=correlation_id)
    s.run()

    return jsonify(status="service ran succesfully")


def start_api():
    serve(app, port=5000)
    # app.run(debug=True, use_reloader=False, port=5000)

if __name__ == '__main__':
    start_api()