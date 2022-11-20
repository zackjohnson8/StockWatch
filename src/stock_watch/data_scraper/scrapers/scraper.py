from abc import ABC, abstractmethod


class Scraper(ABC):
    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...

    @property
    @abstractmethod
    def running(self):
        ...
