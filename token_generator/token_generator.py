from abc import ABC, abstractmethod

class TokenGenerator(ABC):
    def __init__(self, token_provider):
        self.token_provider = token_provider
    @abstractmethod
    def access_token(self, tenant_id: str) -> str:
        pass
