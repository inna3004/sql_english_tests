from service.repository import UsersRepository, TestsRepository
from storage.sqlite_storage import SqliteStorage
from service.auth_service import AuthService
from service.tests_service import TestsService
from service.score_service import ScoreSerive
from interface.auth import Login
from interface.tests import Tests
from service.result_service import ResultService

def main():
    storage = SqliteStorage('./storage/data.db')
    userRepository = UsersRepository(storage)
    testsRepository = TestsRepository(storage)

    auth = AuthService(userRepository)
    testsService = TestsService(testsRepository)
    score = ScoreSerive(testsRepository)

    authInterface = Login(auth)
    testsInterface = Tests(testsService)

    result_service = ResultService(userRepository)

    while True:
        user = authInterface.login_form()
        if user is None:
            continue
        test = testsInterface.choose_test()
        choises = testsInterface.run_test(test)
        sum = score.score(answers=choises, test=test)

        result = result_service.save_result(user=user, test=test, sum=sum)
        print(f"Вы набрали {sum} баллов")
        choose_result(user, result_service)


def choose_result(user, results):
    print(f"Вы хотите увидеть историю результатов тестирования ?")
    choise = input()
    if choise == "yes":
        results = results.get_results_history(user.id)
        for result in results:
            print(result)
        return results
    else:
        exit()

if __name__ == '__main__':

    main()
