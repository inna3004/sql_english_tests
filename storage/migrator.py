from storage.sqlite_storage import SqliteStorage


class Migrator:
    def __init__(self, storage: SqliteStorage):
        self.storage = storage

    def migrate(self):
        query1 = f"""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                text VARCHAR(255) NOT NULL,
                correct_answer_id integer,
                tests_id integer,
                FOREIGN KEY (tests_id) REFERENCES tests(id),
                FOREIGN KEY (correct_answer_id) REFERENCES answers(id)
            )
        """
        self.storage.connection.execute(query1)

        query2 = f"""
            CREATE TABLE IF NOT EXISTS answers (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                value VARCHAR(255) NOT NULL,
                question INT REFERENCES questions(id)
            )
        """
        self.storage.connection.execute(query2)

        query3 = f"""
            CREATE TABLE IF NOT EXISTS tests (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                title  VARCHAR(255) NOT NULL,
                difficult  integer,
                category VARCHAR(255) NOT NULL
            )
        """
        self.storage.connection.execute(query3)

        query4 = f"""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                score integer,
                user_id integer,
                test_id integer,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (test_id) REFERENCES tests(id) ON DELETE CASCADE
            )
        """
        self.storage.connection.execute(query4)

        query5 = f"""
           CREATE TABLE IF NOT EXISTS users (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               username VARCHAR(255) NOT NULL,
               password VARCHAR(255) NOT NULL,
               is_admin BOOLEAN
           )
       """
        self.storage.connection.execute(query5)
        self.storage.connection.commit()


migrator = Migrator(SqliteStorage("data.db"))
migrator.migrate()
