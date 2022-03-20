from models.descriptive import DescriptiveModel


class Scorer:
    def __init__(self):
        pass

    def check_similarity(self, model_answer, given_answer):
        return 1

    def check_keywords(self, given_answer, keywords):
        return 1

    def sentiment_similarity(self, model_answer, given_answer):
        return 1

    def score(self, answer: DescriptiveModel):
        weighted_score: float = (
            0.2*self.check_similarity(answer.model_answer, answer.given_answer)
            + 0.4*self.check_keywords(answer.given_answer, answer.keywords)
            + 0.4*self.sentiment_similarity(answer.model_answer, answer.given_answer)
        )
        
        return weighted_score*answer.weightage
