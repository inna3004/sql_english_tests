from service.models import Test
from service.models import User
from service.repository import TestsRepository, UsersRepository

class ResultService:
    users_repository: UsersRepository

    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    def save_result(self, user: User, test: Test, score: int):
        score = self.users_repository.save_result(user)
    def get_results_history(self, user:User):
        user = self.users_repository.get_users_results(user)