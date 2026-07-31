from abc import ABC, abstractmethod

class Query(ABC):

    @abstractmethod
    def prompt(self) -> str:
        ...

    @abstractmethod
    def command_select(self, command: str, *args, **kwargs):
        ...