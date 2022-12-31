from abc import ABC, abstractmethod


class Scraper(ABC):
    @abstractmethod
    def start(self, conn):
        ...

    @abstractmethod
    def stop(self):
        ...

    @property
    @abstractmethod
    def running(self):
        ...
