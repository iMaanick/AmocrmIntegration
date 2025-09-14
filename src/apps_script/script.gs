function onEdit(e) {
  const base_url = "YOUR_URL_HERE"
  if (!e) {
    Logger.log("Функция вызвана вручную, e отсутствует");
    return;
  }

  const sheet = e.range.getSheet();
  const startRow = e.range.getRow();
  const numRows = e.range.getNumRows();

  if (startRow === 1) return; // пропускаем заголовок

  // читаем заголовки
  const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];

  // словарь "название столбца -> индекс"
  const headerMap = {};
  headers.forEach((h, i) => {
    headerMap[h] = i + 1;
  });

  // читаем диапазон всех изменённых строк
  const rowValues = sheet
    .getRange(startRow, 1, numRows, sheet.getLastColumn())
    .getValues();

  for (let i = 0; i < numRows; i++) {
    const rowIndex = startRow + i;
    if (rowIndex === 1) continue; // не трогаем заголовки

    const values = rowValues[i];

    const payload = {
      row: rowIndex,
      email: values[headerMap["email"] - 1],
      amount: values[headerMap["amount"] - 1],
    };

    const url =  base_url + "/leads/upsert";
    const options = {
      method: "post",
      contentType: "application/json",
      payload: JSON.stringify(payload),
    };

    try {
      const response = UrlFetchApp.fetch(url, options);
      sheet.getParent().toast("Row " + rowIndex + " response: " + response.getContentText());
      Logger.log("Row " + rowIndex + " response: " + response.getContentText());
    } catch (err) {
      sheet.getParent().toast("Ошибка запроса (row " + rowIndex + "): " + err);
      Logger.log("Ошибка запроса (row " + rowIndex + "): " + err);
    }
  }
}
