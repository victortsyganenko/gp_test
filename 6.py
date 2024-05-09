import pandas as pd

from datetime import datetime
from http import HTTPStatus
from json import loads
from pydantic import BaseModel, Field
from requests import get
from sys import exit
from typing import List, Tuple


class RequestResponse(BaseModel):
    Columns: List[str] = Field(min_items=3, max_items=3)
    Description: str
    RowCount: int
    Rows: List[Tuple[int, datetime, str]]

    @staticmethod
    def get_rows_mapping_dict() -> dict:
        return {
            'key1': 'document_id',
            'key2': 'document_dt',
            'key3': 'document_name'
        }


if __name__ == "__main__":
    start_date_timestamp = int(
        datetime.now()
        .replace(hour=0, minute=0, second=0, microsecond=0)
        .timestamp()
    )
    try:
        result = get(
            'https://api.gazprombank.ru/very/important/docs',
            params={
                'documents_date': str({f'"{start_date_timestamp}"'})
            },
            headers={
                'accept': 'application/json'
            }
        )
        if result.status_code != HTTPStatus.OK:
            print(
                f'API вернул ошибку. Код {result.status_code}.\n'
                f'Причина: {result.reason}\n'
                f'Ответ: {result.content.decode()}'
            )
            exit(-1)
    except Exception as e:
        print(f'Ошибка запроса данныз по API: {e}')
        exit(-1)

    try:
        result = RequestResponse(**loads(result.content))
    except Exception as e:
        print(
            f'Ошибка парсинга ответа API: {e}\n'
            f'Ответ: {result.content.decode()}'
        )
        exit(-1)

    result = pd.DataFrame(result.Rows, columns=result.Columns)
    result.rename(
        columns=RequestResponse.get_rows_mapping_dict(),
        inplace=True
    )
    result['load_dt'] = datetime.now()

    print(result.to_string())
