from storage.sqlite_storage import SqliteStorage
from service.models import Test, Question, Answer, User


class BaseRepository:
    def __init__(self, storage: SqliteStorage):
        self.storage = storage


class TestsRepository(BaseRepository):
    def get_tests(self):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM tests;"
        cursor.execute(query)
        rows = cursor.fetchall()
        tests = []
        for row in rows:
            test = Test(row[1], row[2], row[3], row[0])
            tests.append(test)
        return tests




    def find_question(self, question_id):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM questions;"
        cursor.execute(query)
        rows = cursor.fetchone()
        question = Question(rows[1])
        question.id = rows[0]
        question.question_id = rows[1]



    def find_all_answer(self, data: list|tuple, question_id: int):
        answers = []
        for row in data:
            if row[4] != question_id:
                continue
            answers.append(Answer(value=row[9], id=row[8]))
        return answers

    def get_correct_answer(self, data: list|tuple, correct_answer_id: int):
        for row in data:
            if row[6] != correct_answer_id:
                continue
            return Answer(value=row[9], id=row[8])

    def get_full_test(self, test_id: int):
        cursor = self.storage.connection.cursor()
        query = f"""
            SELECT * FROM tests
            JOIN questions ON tests.id = questions.tests_id
            JOIN answers ON answers.question = questions.id
            WHERE tests.id = {test_id}
            order by questions.id;
        """
        cursor.execute(query)
        raw_data = cursor.fetchall()

        test = Test(test_id=raw_data[0][0], title=raw_data[0][1], difficult=raw_data[0][2], category=raw_data[0][3])
        test.questions = []
        for row in raw_data:
            question_id = row[4]
            if len(test.questions) == 0 or question_id != test.questions[-1].id:
                question = Question(id=row[4], text=row[5])
                question.answers = self.find_all_answer(raw_data, question.id)
                question.correct_answer = self.get_correct_answer(raw_data, row[6])
                test.questions.append(question)

        return test


class UsersRepository(BaseRepository):
    def get_user(self, users_id):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM users WHERE id = {users_id};"
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows

    def title_tests(self, tests_id):
        cursor = self.storage.connection.cursor()
        query = f"SELECT title FROM tests where id = {tests_id};"
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows


    def get_by_username(self, username: str):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}';"
        cursor.execute(query)
        rows = cursor.fetchone()
        if rows is None:
            return None
        user = User()
        user.id = rows[0]
        user.username = rows[1]
        user.password = rows[2]
        user.is_admin = rows[3]
        return user

    def save_result(self, user: User, test: Test, result: int):
        pass

    def get_users_results(self, user: User):
        pass


