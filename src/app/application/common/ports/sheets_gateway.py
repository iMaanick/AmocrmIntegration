from abc import ABC, abstractmethod


class SheetsGateway(ABC):
    @abstractmethod
    def update_lead(self, row_id: int, email: str, amount: int) -> None:
        raise NotImplementedError
