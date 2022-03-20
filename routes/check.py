from fastapi import APIRouter, status, HTTPException
from models.descriptive import DescriptiveModel
from scripts.utils.scorer import Scorer

router = APIRouter(tags=["Check"], prefix="/check")


@router.post("/descriptive/")
async def check_descriptive(answer: DescriptiveModel, status_code=status.HTTP_200_OK):
    """**Summary**:
        Checks for relevance of descriptive answer.


    **Request type**: POST


    **Request body type**:

        answer: string containing answer given by participant
        keywords: Optional list of strings containing keywords for the answer
        model_answer: Optional string containing model answer


    **Returns**:
        Dictionary/Object: Containing relevance score
    """

    scorer = Scorer()
    return {"score": scorer.score(answer)} #, "weightage": answer.weightage}
