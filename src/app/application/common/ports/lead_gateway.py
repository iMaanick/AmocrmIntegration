from abc import ABC, abstractmethod

from app.application.common.ports.lead_dto import LeadCreate


class LeadGateway(ABC):
    @abstractmethod
    def create(self, lead: LeadCreate) -> int:
        raise NotImplementedError