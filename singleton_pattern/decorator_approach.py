from typing import Any, Callable


def singleton(cls: type) -> Callable[..., Any]:
    instance: dict[type, Any] = {}

    def get_instance(*args: Any, **kwargs: Any) -> Any:
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance


@singleton
class AppConfig:
    def __init__(self) -> None:
        print("Loading Configuration")
        self.debug_mode: bool = True
        self.api_key: str = "secret-key-123"
        self.max_connection: int = 100
        self.timeout: int = 30

    def update_setting(self, key: str, value: Any) -> None:
        setattr(self, key, value)
        print(f"Update {key} = {value}")


config1 = AppConfig()

print(f"Debug mode: {config1.debug_mode}")


# Second access - no re-initialization
print("\nAccessing config again:")
config2 = AppConfig()
config2.update_setting("timeout", 60)

print(f"\nconfig1 timeout: {config1.timeout}")
print(f"Same instance? {config1 is config2}")
