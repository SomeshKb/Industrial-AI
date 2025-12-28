import uuid
from ..db import db
from ..constants.status import StatusEnum


class AnomalyModel(db.Model):
    __tablename__ = "anomaly_models"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False, default=StatusEnum.DRAFT.value)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "status": self.status}
