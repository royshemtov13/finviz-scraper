import os
import time
from pathlib import Path

import pandas as pd
import user_agent
from mechanicalsoup import StatefulBrowser

from scraper.models.screener import Screener


class FinvizScraper:
    def __init__(self, download_dir: str = "/tmp"):
        self.download_dir = download_dir
        self.files = []
        self.browser = StatefulBrowser(
            soup_config={"features": "lxml"},
            user_agent=user_agent.generate_user_agent(),
            raise_on_404=True,
        )

    def __enter__(self):
        self.login()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.close()

    def login(self):
        self.browser.open("http://finviz.com", verify=True)
        self.browser.follow_link("login")
        self.browser.select_form('form[name="login"]')
        self.browser["email"] = os.environ["FINVIZ_USERNAME"]
        self.browser["password"] = os.environ["FINVIZ_PASSWORD"]
        self.browser["remember"] = True
        response = self.browser.submit_selected()

        assert response.status_code == 200

    def download_data(self, screener: Screener):
        url = self._create_url(filters=screener.encode())
        filepath = Path(self.download_dir) / f"{screener.name}.csv"

        self.browser.open(url, verify=True)
        self.browser.download_link("export", file=filepath)

        time.sleep(1)

        assert filepath.exists()
        self.files.append(filepath)

    def read_data(self, screeners: list[Screener]) -> pd.DataFrame:
        data = pd.DataFrame()
        for csv_file in self.files:
            csv = pd.read_csv(csv_file, index_col=0)
            if csv.empty:
                continue
            self._add_metadata(csv_file, csv, screeners)
            data = pd.concat([data, csv], axis=0)
        return data

    @staticmethod
    def _create_url(filters: str) -> str:
        settings = (
            "&ft=4&o=-change&c=0,1,2,79,3,4,5,6,7,8,9,10,11,12,13,73,74,75,14,15,16,77,17,18,19,20,21,23,22,"
            "82,78,24,25,85,26,27,28,29,30,31,84,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,"
            "52,53,54,55,56,57,58,59,68,70,80,83,76,60,61,62,63,64,67,69,81,86,87,88,65,66,71,72"
        )

        url = "https://elite.finviz.com/screener.ashx"
        params = {"v": 151, "f": filters}
        for key, value in params.items():
            prefix = "?" if key == "v" else "&"
            url += f"{prefix}{key}={value}"
        return url + settings

    @staticmethod
    def _add_metadata(
        csv_file: Path, data: pd.DataFrame, screeners: list[Screener]
    ) -> pd.DataFrame:
        screener_name = csv_file.name.rstrip(".csv")
        screener = [
            screener for screener in screeners if screener.name == screener_name
        ][0]
        return data
