import duckdb
from constants import DATABASE_PATH


class Database:
    
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.connection = None
    
    def __enter__(self):
        self.connection = duckdb.connect(self.db_path)
        return self
    
    def query(self, query):
        return self.connection.execute(query).fetchall()
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
            
            
if __name__ == "__main__":     
    with Database(DATABASE_PATH) as db:
        query1 = db.query("SELECT * FROM information_schema.schemata;")
    
    print(query1)