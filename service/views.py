from storage.sqlite_storage import SqliteStorage
from storage.migrator import Migrator
migrator = Migrator(SqliteStorage("data.db"))
migrator.migrate()

def get_questions(self):
    cursor = self.storage.connection.cursor()
    query = "SELECT * FROM questions;"
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

def get_answers(self,question_id):
    cursor = self.storage.connection.cursor()
    query = f"SELECT * FROM answers WHERE id = {question_id};"
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

  