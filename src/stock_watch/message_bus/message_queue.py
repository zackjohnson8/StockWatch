from typing import Any, TypeVar
from .models.subscription import Subscription
from .models.publish import Publish

T = TypeVar('T', Publish, Subscription)


class MessageQueue:
    def __init__(self):
        self._queue = []

    def put(self, command: T) -> None:
        self._queue.append(command)

    def get(self) -> T:
        return self._queue.pop(0)

    def __len__(self) -> int:
        return len(self._queue)

    def __iter__(self) -> Any:
        return iter(self._queue)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._queue})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._queue})"
