from flask import Blueprint, request, jsonify
from db import db
from models import Anomaly_Model
model_bp = Blueprint("/", __name__)


@model_bp.route("/", methods=["GET"])
def hello():
    items = Anomaly_Model.query.all()
    return jsonify([item.to_dict() for item in items]), 200

@model_bp.route("/", methods=["POST"])
def create_item():
    data = request.get_json()
    name = data["name"]

    anomaly_Model = Anomaly_Model(name=name)
    db.session.add(anomaly_Model)
    db.session.commit()

    return jsonify(anomaly_Model.to_dict()), 201