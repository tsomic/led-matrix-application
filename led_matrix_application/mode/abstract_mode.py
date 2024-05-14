from abc import ABC, abstractmethod

class AbstractMode(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def update_settings(self, settings):
        pass

    @abstractmethod
    def update_display(self, matrix):
        pass