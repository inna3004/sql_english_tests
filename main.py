from service.repository import UsersRepository, TestsRepository
from storage.sqlite_storage import SqliteStorage
from service.auth_service import AuthService
from service.tests_service import TestsService
from interface.auth import Login
from interface.tests import Tests


def main():
    storage = SqliteStorage('./storage/data.db')
    userRepository = UsersRepository(storage)
    testsRepository = TestsRepository(storage)

    auth = AuthService(userRepository)
    testsService = TestsService(testsRepository)

    authInterface = Login(auth)
    testsInterface = Tests(testsService)

    while True:
        user = authInterface.login_form()
        if user is None:
            continue
        test = testsInterface.choose_test()
        choises = testsInterface.run_test(test)


if __name__ == '__main__':
    main()
