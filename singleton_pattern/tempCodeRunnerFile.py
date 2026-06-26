

@singleton
class AppConfig:
    def __init__(self) -> None:
        print("Loading Configuration")
        self.debug_mode: bool = True
        self.api_key: str = "secret-key-123"
        self.max_connection: int = 100
        self.timeout: int = 30

    def update_setting