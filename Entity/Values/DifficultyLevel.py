from enum import Enum 

class DifficultyLevel(Enum):
    EASY = {"bottom": 6, "top": 8}
    MEDIUM = {"bottom": 3, "top": 6}
    HARD = {"bottom": 2, "top": 5}