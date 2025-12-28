from flask import request, jsonify
from db import db
from models import Anomaly_Model

def get_all():
    models = Anomaly_Model.query.all()
    return jsonify([model.to_dict() for model in models]), 200

def create(name):
    anomaly_Model = Anomaly_Model(name=name)
    db.session.add(anomaly_Model)
    db.session.commit()
    return jsonify(anomaly_Model.to_dict()), 201

def get_by_id(model_id):
    model = Anomaly_Model.query.filter_by(id=model_id).first()

    if not model:
        return jsonify({"error": "Model not found"}), 404

    return jsonify(model.to_dict()), 200