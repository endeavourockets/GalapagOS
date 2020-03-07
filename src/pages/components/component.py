from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def create(self, **args):
        pass
