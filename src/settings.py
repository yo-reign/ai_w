from enum import Enum

class ModelType(Enum):
    REGULAR = 1
    MULTIMODAL = 2

class Config:
    def __init__(self, model_type: ModelType, user_name: str, assistant_name: str, chance_of_responding: float):
        self.model_type = model_type
        self.user_name = user_name
        self.assistant_name = assistant_name
        self.chance_of_responding = chance_of_responding # Set to 1 to always respond, 0 to never respond, 0.5 to half the time, etc.
