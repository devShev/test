import json
from enum import Enum
from string import Template
from typing import Any

import requests

from .schemas import CardResponseSchema
from ..models import CardData


class DataType(Enum):
    CARD = "CARD"
    PRICE_HISTORY = "PRICE_HISTORY"
    INFO = "INFO"


class WBCardParser:
    __URLS_TEMPLATES = {
        DataType.CARD: Template(
            "https://basket-$host.wbbasket.ru/vol$vol/part$part/$article/info/ru/card.json"  # noqa: E501
        ),
        DataType.PRICE_HISTORY: Template(
            "https://basket-$host.wbbasket.ru/vol$vol/part$part/$article/info/price-history.json"  # noqa: E501
        ),
        DataType.INFO: Template(
            "https://card.wb.ru/cards/v2/detail?appType=1&curr=byn&dest=-59202&spp=30&ab_testing=false&nm=$article"  # noqa: E501
        ),
    }

    BASKET_RANGES = [
        (0, 143, "01"),
        (144, 287, "02"),
        (288, 431, "03"),
        (432, 719, "04"),
        (720, 1007, "05"),
        (1008, 1061, "06"),
        (1062, 1115, "07"),
        (1116, 1169, "08"),
        (1170, 1313, "09"),
        (1314, 1601, "10"),
        (1602, 1655, "11"),
        (1656, 1919, "12"),
        (1920, 2045, "13"),
        (2046, 2189, "14"),
        (2190, 2405, "15"),
        (2406, 2621, "16"),
        (2622, 2837, "17"),
    ]

    def __init__(self) -> None:
        self._session = requests.Session()

    @classmethod
    def __get_basket_prefix(cls, vol: int) -> str:
        host = next(
            (
                host
                for start, end, host in cls.BASKET_RANGES
                if start <= vol <= end
            ),
            "18",
        )
        return host

    @classmethod
    def __generate_url(
        cls,
        template: Template,
        article: str,
    ) -> str:
        if len(article) == 9:
            vol = article[:4]
            part = article[:6]
        else:
            vol = article[:3]
            part = article[:5]

        host = cls.__get_basket_prefix(int(vol))

        return template.substitute(
            {
                "vol": vol,
                "part": part,
                "article": article,
                "host": host,
            }
        )

    def __get_response(
        self,
        article: str,
        data_type: DataType = DataType.CARD,
    ) -> requests.Response:
        template = self.__URLS_TEMPLATES.get(data_type)

        if not template:
            raise ValueError("BAD DataType value")

        response = self._session.get(self.__generate_url(template, article))
        return response

    def get_card_data(self, article: str) -> CardResponseSchema:
        return CardResponseSchema.model_validate_json(
            self.__get_response(article, DataType.CARD).text
        )

    def get_price_history_data(self, article: str) -> Any:
        return json.loads(
            self.__get_response(article, DataType.PRICE_HISTORY).text
        )

    def get_info_data(
        self,
        article: str,
    ) -> Any:
        return self.__get_response(article, DataType.INFO).json()

    def save_to_db(
        self,
        article: str,
    ) -> None:
        instance = CardData(article, **self.parse_by_article(article))
        instance.save()

    def parse_by_article(
        self,
        article: str,
    ) -> dict[str, Any]:
        return {
            "card_data": self.get_card_data(article).model_dump_json(),
            "price_history_data": self.get_price_history_data(article),
            "info_data": self.get_info_data(article),
        }
