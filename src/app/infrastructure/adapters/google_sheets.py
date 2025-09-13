from typing import NewType

from gspread import Client, Worksheet

from app.application.common.ports.sheets_gateway import SheetsGateway

GoogleCreds = NewType("GoogleCreds", dict[str, str])
SpreadsheetUrl = NewType("SpreadsheetUrl", str)
SpreadsheetName = NewType("SpreadsheetName", str)


class GoogleSheetsGateway(SheetsGateway):
    def __init__(
            self,
            client: Client,
            spreadsheet_url: SpreadsheetUrl,
            spreadsheet_name: SpreadsheetName,
    ) -> None:
        self.client = client
        self.spreadsheet_url = spreadsheet_url
        self.spreadsheet_name = spreadsheet_name

    def _get_worksheet(self, name: str) -> Worksheet:
        spreadsheet = self.client.open_by_url(self.spreadsheet_url)
        return spreadsheet.worksheet(name)

    def update_lead(self, row_id: int, email: str, amount: int) -> None:
        sheet = self._get_worksheet(self.spreadsheet_name)
        sheet.update_cell(row_id, 1, email)
        sheet.update_cell(row_id, 2, amount)
