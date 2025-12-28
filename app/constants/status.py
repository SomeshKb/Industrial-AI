from enum import Enum


class StatusEnum(str, Enum):
    DRAFT = "Draft"
    TRAINED = "Trained"
    TRAINING_IN_PROGRESS = "Training in Progress"
    TRAINING_FAILED = "Training Failed"
