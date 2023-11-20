from scraper.screener.etl import FinvizETL
from scraper.screener.screeners import Screeners
from scraper.utils.config import get_config


def main():
    config = get_config("screeners.yaml")
    filters = [filt["name"] for filt in config]
    etl = FinvizETL()
    screeners = Screeners.from_filters(filters)
    data = etl.extract(screeners).transform().load()
    return data["ticker"]


if __name__ == "__main__":
    main()
