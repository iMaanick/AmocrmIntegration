from abc import ABC, abstractmethod

from app.application.common.ports.lead_dto import LeadCreate, LeadUpdate


class LeadGateway(ABC):
    @abstractmethod
    def create(self, lead: LeadCreate) -> int:
        raise NotImplementedError

    @abstractmethod
    def update(self, lead_id: int, data: LeadUpdate) -> None:
        raise NotImplementedError
