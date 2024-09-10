from storage.sqlite_storage import SqliteStorage


class Migrator:
    def __init__(self, storage: SqliteStorage):
        self.storage = storage


    def migrate(self):
        query1 = f"CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY, text TEXT)"
        self.storage.connection.execute(query1)

        query2 = f"""
            CREATE TABLE IF NOT EXISTS answers (
                id INTEGER PRIMARY KEY,
                value TEXT,
                FOREIGN KEY (id) REFERENCES questions(id) ON DELETE CASCADE
            )
        """
        self.storage.connection.execute(query2)

        query3 = f"""
            CREATE TABLE IF NOT EXISTS tests (
                id INTEGER PRIMARY KEY,
                value TEXT,
                FOREIGN KEY (id) REFERENCES questions(id) ON DELETE CASCADE
            )
        """
        self.storage.connection.execute(query3)

        query4 = f"""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY,
                value TEXT,
                FOREIGN KEY (id) REFERENCES questions(id) ON DELETE CASCADE
            )
        """
        self.storage.connection.execute(query4)

        query5 = f"""
           CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               value TEXT,
               FOREIGN KEY (id) REFERENCES questions(id) ON DELETE CASCADE
           )
       """
        self.storage.connection.execute(query5)
        self.storage.connection.commit()

        migrator = Migrator(SqliteStorage("data.db"))
        migrator.migrate()
