from flask import Blueprint, request, jsonify
from ...services.anomaly_model_service import list_models, create_model, get_model_by_id
from ...schemas.anomaly_model_schema import create_schema, list_schema
from ...core.exceptions import NotFoundError, ValidationError

bp = Blueprint("anomaly_models", __name__)


@bp.route("/", methods=["GET"])
def get_models():
    # pagination & filtering
    try:
        limit = int(request.args.get("limit", 100))
        offset = int(request.args.get("offset", 0))
    except ValueError:
        return jsonify({"error": "limit and offset must be integers"}), 400

    filters = {}
    status = request.args.get("status")
    name = request.args.get("name")
    if status:
        filters["status"] = status
    if name:
        filters["name"] = name

    models = list_models(filters=filters, limit=limit, offset=offset)
    return jsonify(list_schema.dump(models)), 200


@bp.route("/", methods=["POST"])
def post_model():
    json_data = request.get_json() or {}
    try:
        data = create_schema.load(json_data)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400

    model = create_model(data)
    return jsonify(create_schema.dump(model)), 201


@bp.route("/<string:model_id>", methods=["GET"])
def get_model(model_id: str):
    try:
        model = get_model_by_id(model_id)
    except NotFoundError as exc:
        return jsonify({"error": str(exc)}), 404

    return jsonify(create_schema.dump(model)), 200
