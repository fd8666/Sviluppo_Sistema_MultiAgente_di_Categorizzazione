
from pydantic import BaseModel, Field
from enum import Enum
from typing import List

class Season(str, Enum):
    SUMMER = "Summer"
    SPRING = "Spring"
    AUTUMN = "Autumn"
    WINTER = "Winter"
    NA = "N/A"

class ThemesOutput(BaseModel):
    tags: List[str] =Field(
        min_length=5,  
        max_length=15
    )

class CategoryOutput(BaseModel):
    category : Season


class EvaluatorOutput(BaseModel):
    confidence: int = Field(
        ge=0, 
        le=100
    )
