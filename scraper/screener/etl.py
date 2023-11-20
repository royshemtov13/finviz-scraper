import pandas as pd
from loguru import logger
from mechanicalsoup import LinkNotFoundError

from scraper.exceptions import EmptyDataFrame
from scraper.models.screener import Screener
from scraper.screener.scraper import FinvizScraper
from scraper.utils import snake_case


class FinvizETL:
    def __init__(self, download_dir: str = "/tmp"):
        self.download_dir = download_dir
        self.scraper = FinvizScraper(self.download_dir)
        self.data = pd.DataFrame()
        self.table_name = "watchlist"

    def extract(self, screeners: list[Screener]):
        logger.info("Extracting data from Finviz...")
        with self.scraper as scraper:
            for screener in screeners:
                try:
                    scraper.download_data(screener)
                except LinkNotFoundError:
                    continue
        self.data = scraper.read_data(screeners)
        return self

    def transform(self):
        if self.data.empty:
            raise EmptyDataFrame
        self.data.columns = [snake_case(col) for col in self.data.columns]

        self.data = self.data.reset_index(drop=True)
        self.data.index += 1

        return self

    def load(self) -> pd.DataFrame:
        return self.data
