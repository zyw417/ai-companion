from abc import ABC, abstractmethod


class BaseModel(ABC):

    @abstractmethod
    async def chat(self, message: str) -> str:
        pass
