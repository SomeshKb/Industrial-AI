from flask import Blueprint, request, jsonify
from models import Anomaly_Model
from services import anomaly_model_service
model_bp = Blueprint("/", __name__)


@model_bp.route("/", methods=["GET"])
def hello():
    return anomaly_model_service.get_all()

@model_bp.route("/", methods=["POST"])
def create_item():
        data = request.get_json()
        name = data["name"]
        return anomaly_model_service.create_anomaly_model(name)

@model_bp.route("/<string:model_id>", methods=["GET"])
def get_model_by_id(model_id):
      return anomaly_model_service.get_by_id(model_id)