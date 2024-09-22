from service.repository import Repository
from storage.sqlite_storage import SqliteStorage

def main():
    storage = SqliteStorage('./storage/data.db')
    repo = Repository(storage)
    test = repo.get_full_test(1)
    for question in test.questions:
        print(question)
        print('Варианты ответа:')
        for i in range(0, len(question.answer)):
            print(i + 1, question.answer[i])
        print('введите номер выбранного ответа:')
        choise = input()

if __name__ == '__main__':
    main()
