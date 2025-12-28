from db import db
import uuid
from constants.status import StatusEnum


class Anomaly_Model(db.Model):
    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False, default=StatusEnum.DRAFT)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status
        }
