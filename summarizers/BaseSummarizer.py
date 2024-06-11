from abc import ABC, abstractmethod
from configparser import ConfigParser


class BaseSummarizer(ABC):
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('config.ini')

    @abstractmethod
    def summarize_text(self, text):
        pass
