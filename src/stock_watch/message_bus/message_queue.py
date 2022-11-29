from typing import Any


class MessageQueue:
    def __init__(self):
        self._queue = []

    def put(self, command: Any) -> None:
        self._queue.append(command)

    def get(self) -> Any:
        return self._queue.pop(0)

    def __len__(self) -> int:
        return len(self._queue)

    def __iter__(self) -> Any:
        return iter(self._queue)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._queue})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._queue})"

    def empty(self):
        return len(self._queue) == 0
