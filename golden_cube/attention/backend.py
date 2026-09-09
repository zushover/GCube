from abc import ABC, abstractmethod


class AttentionBackend(ABC):
    @abstractmethod
    def forward(self, *args, **kwargs):
        raise NotImplementedError
