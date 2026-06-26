class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new database connection")
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            print("Initializing the database connection")
            self.connection_string = "postgresql:://localhost/my_db"
            self.pool_size = 10
            self._initialized = True

    def query(self, sql):
        return f"Executing : {sql}"


db1 = DatabaseConnection()
print(f"db1 connection: {db1.connection_string}")

print("Creating second instance")
db2 = DatabaseConnection()
print(f"db2 connection : {db2.connection_string}")

print(f"\nAre they the same object? {db1 is db2}")
