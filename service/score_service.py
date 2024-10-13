from service.models import Test
from service.repository import TestsRepository, UsersRepository


class ScoreSerive:
    def __init__(self, tests_repository: TestsRepository) -> None:
        self.tests_repository = tests_repository

    def score(self, answers: dict, test: Test):
        test = self.tests_repository.get_full_test(test.id)
        sum = 0
        for questionId, answerId in answers.items():
            for question in test.questions:
                if question.id == questionId:
                    if question.correct_answer.id == answerId:
                        sum += 1
        return sum

