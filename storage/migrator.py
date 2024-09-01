from storage.sqlite_storage import SqliteStorage


class Migrator:
    def __init__(self, storage: SqliteStorage):
        self.storage = storage

    def migrate(self):
        self.storage.connection.execute("""
        
        """)