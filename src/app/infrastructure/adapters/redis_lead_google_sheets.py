from typing import cast, Any

from redis import Redis

from app.application.common.ports.sheets_lead_gateway import SheetsLeadGateway


class RedisSheetsLeadGateway(SheetsLeadGateway):
    def __init__(self, client: Redis):
        self.client = client
        self.prefix = "google_sheets_"

    def set_lead(self, row_id: int, lead_id: int) -> None:
        self.client.set(f"{self.prefix}row:{row_id}", lead_id)
        self.client.set(f"{self.prefix}lead:{lead_id}", row_id)

    def get_lead(self, row_id: int) -> int | None:
        value = cast(Any, self.client.get(self.prefix + str(row_id)))
        return int(value) if value is not None else None

    def get_row_by_lead(self, lead_id: int) -> int | None:
        value = cast(Any, self.client.get(f"{self.prefix}lead:{lead_id}"))
        return int(value) if value is not None else None
