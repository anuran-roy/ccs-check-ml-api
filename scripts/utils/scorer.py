from models.descriptive import DescriptiveModel
import spacy


class Scorer:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except Exception:
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

    def check_similarity(self, model_answer, given_answer):
        if model_answer is None:
            return 1

        if given_answer is None or given_answer == "":
            return 0

        model_answer_token = self.nlp(model_answer)
        given_answer_token = self.nlp(given_answer)

        return given_answer_token.similarity(model_answer_token)

    def check_keywords(self, given_answer, keywords):
        if keywords is []:
            return 1

        received_keywords = [x.lemma_ for x in self.nlp(given_answer)]
        common_keywords = set(keywords).intersection(set(received_keywords))
        return len(common_keywords) / len(set(keywords))  # Score

    def sentiment_similarity(self, model_answer, given_answer):
        return 1

    def score(self, answer: DescriptiveModel):
        weighted_score: float = (
            # 0.2 * self.check_similarity(
            #     answer.model_answer, answer.given_answer
            # ) +
            0.6 * self.check_keywords(answer.given_answer, answer.keywords)
            + 0.4 * self.check_similarity(
                answer.model_answer, answer.given_answer
            ) 
        )

        return weighted_score * answer.weightage
