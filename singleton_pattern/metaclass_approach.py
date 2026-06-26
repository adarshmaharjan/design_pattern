from typing import Any


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"[LOG] {message}")

    def get_log(self):
        return self.log


logger1 = Logger()
logger1.log("Application started")
logger1.log("User logged in")

# Another part of code gets the same logger
logger2 = Logger()
logger2.log("Processing request")

print(f"\nTotal logs in logger1: {len(logger1.get_logs())}")
print(f"Total logs in logger2: {len(logger2.get_logs())}")
print(f"Same logger? {logger1 is logger2}")
