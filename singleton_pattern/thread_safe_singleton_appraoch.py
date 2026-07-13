import threading
from typing import Optional


class ThreadSafeSingleton:
    """
    Thread safe singleton approach
    """

    _instance: Optional["ThreadSafeSingleton"] = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print(f"Thread {threading.current_thread().name}: Creating Instance")
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            with self._lock:
                if not self._initialized:
                    print(f"Thread {threading.current_thread().name}: Initializing")
                    self.data = {}
                    self._initialized = True


def create_singleton(thread_id):
    instance = ThreadSafeSingleton()
    instance.data[thread_id] = f"Data from thread {thread_id}"


threads = []
for i in range(5):
    t = threading.Thread(target=create_singleton, args=(i,), name=f"Thread-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Verify it's a singleton
final = ThreadSafeSingleton()
print(f"\nShared data across all threads: {final.data}")
