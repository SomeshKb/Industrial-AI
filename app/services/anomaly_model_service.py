from typing import Dict, Any, List, Optional
from ..db import db
from ..models.anomaly_model import AnomalyModel
from ..core.exceptions import NotFoundError


def list_models(filters: Optional[Dict[str, Any]] = None, limit: int = 100, offset: int = 0) -> List[AnomalyModel]:
    query = AnomalyModel.query

    if filters:
        if "status" in filters:
            query = query.filter_by(status=filters["status"])
        if "name" in filters:
            query = query.filter(AnomalyModel.name.ilike(f"%{filters['name']}%"))

    return query.offset(offset).limit(limit).all()


def create_model(data: Dict[str, Any]) -> AnomalyModel:
    model = AnomalyModel(name=data["name"], status=data.get("status", AnomalyModel.status.default.arg))
    db.session.add(model)
    db.session.commit()
    return model


def get_model_by_id(model_id: str) -> AnomalyModel:
    model = AnomalyModel.query.filter_by(id=model_id).first()
    if not model:
        raise NotFoundError(f"Model with id {model_id} not found")
    return model
