from abc import ABC, abstractmethod


class SheetsLeadGateway(ABC):

    @abstractmethod
    def set_lead(self, row_id: int, lead_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_lead(self, row_id: int) -> int | None:
        raise NotImplementedError

    @abstractmethod
    def get_row_by_lead(self, lead_id: int) -> int | None:
        raise NotImplementedError
