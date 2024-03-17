from flask import Blueprint, jsonify, current_app
import random

from service.service import Service


bp = Blueprint('main', __name__)

@bp.route('/health')
def health():
    current_app.logger.info('Health check requested')
    return jsonify(status="OK")


@bp.route('/run-service')
def run_service():
    correlation_id = f"correlation-id-api-request-{random.randint(1, 999999)}"
    s = Service(correlation_id=correlation_id)
    s.run()

    return jsonify(status="service ran succesfully")
