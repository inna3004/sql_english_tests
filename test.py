from service.repository import UsersRepository, TestsRepository
from storage.sqlite_storage import SqliteStorage

storage = SqliteStorage('./storage/data.db')
userRepository = UsersRepository(storage)

res = userRepository.get_users_results(1)

print(res)