from scraper.exceptions import InvalidFilterException
from scraper.models.screener import Screener
from scraper.utils.config import get_config


class Screeners:
    config = get_config("screeners.yaml")

    @classmethod
    def from_filters(cls, filters: list[str]) -> list[Screener]:
        cls._validate(filters)
        screeners = cls._parse(filters)
        return screeners

    @classmethod
    def _parse(cls, filters: list[str]) -> list[Screener]:
        screeners = [
            Screener(name=screener["name"], filters=screener["filters"])
            for screener in map(dict, cls.config)
            if screener["name"] in filters
        ]
        return screeners

    @classmethod
    def _validate(cls, filters: list[str]):
        available_filters = [fltr["name"] for fltr in map(dict, cls.config)]
        if not all([fltr in available_filters for fltr in filters]):
            raise InvalidFilterException
