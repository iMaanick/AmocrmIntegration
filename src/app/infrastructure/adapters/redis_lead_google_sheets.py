from typing import cast, Any

from redis import Redis

from app.application.common.ports.sheets_lead_gateway import SheetsLeadGateway


class RedisSheetsLeadGateway(SheetsLeadGateway):
    def __init__(self, client: Redis):
        self.client = client
        self.prefix = "google_sheets_"

    def set_lead(self, row_id: int, lead_id: int) -> None:
        self.client.set(self.prefix + str(row_id), str(lead_id))

    def get_lead(self, row_id: int) -> int | None:
        value = cast(Any, self.client.get(self.prefix + str(row_id)))
        return int(value) if value is not None else None

    def delete_lead(self, row_id: int) -> None:
        self.client.delete(self.prefix + str(row_id))

    def exists(self, row_id: int) -> bool:
        return bool(self.client.exists(self.prefix + str(row_id)))
