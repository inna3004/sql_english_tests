from service.repository import UsersRepository, TestsRepository
from storage.sqlite_storage import SqliteStorage
from service.auth_service import AuthService
from service.tests_service import TestsService
from service.score_service import ScoreSerive
from interface.auth import Login
from interface.tests import Tests
from service.result_service import ResultService
from service.result_service import Results

def main():
    storage = SqliteStorage('./storage/data.db')
    userRepository = UsersRepository(storage)
    testsRepository = TestsRepository(storage)

    auth = AuthService(userRepository)
    testsService = TestsService(testsRepository)
    score = ScoreSerive(testsRepository)

    authInterface = Login(auth)
    testsInterface = Tests(testsService)

    def choose_result():
        print(f"Вы хотите увидеть историю результатов тестирования ?")
        choise = input()
        if choise == "yes":
            results = Results()
            get_result = results.get_results_history()
            print(get_result)
            return get_result
        else:
            exit()

    while True:
        user = authInterface.login_form()
        if user is None:
            continue
        test = testsInterface.choose_test()
        choises = testsInterface.run_test(test)
        sum = score.score(answers=choises, test=test)
        result_service = ResultService(userRepository)
        result = result_service.save_result(user=user, test=test, sum=sum)
        print(f"Вы набрали {sum} баллов")
        choose_result()




if __name__ == '__main__':

    main()
