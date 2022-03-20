from pydantic import BaseModel
from typing import Optional, List


class DescriptiveModel(BaseModel):
    given_answer: str
    keywords: Optional[List[str]] = []
    model_answer: Optional[str] = None
    weightage: Optional[float] = 1
