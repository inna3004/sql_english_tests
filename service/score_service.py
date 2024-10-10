from service.models import Test

class ScoreSerive:

    def __init__(self) -> None:
        pass

    def score(self, answers: dict, test: Test):
        sum = 0
        for questionId, answerId in answers.items():
            for question in test.questions:
                if question.id == questionId:
                    if question.correct_answer.id == answerId:
                        sum += 1
        self.save_score(sum)
        return sum


    def save_score(self, sum: int):
        pass
