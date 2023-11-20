import pytest

from scraper.models.screener import Screener
from scraper.screener.screeners import Screeners


@pytest.fixture()
def screeners() -> list[Screener]:
    filters = ["today_up", "today_down"]
    return Screeners.from_filters(filters)


def get_screener_by_name(screeners: list[Screener], name: str) -> Screener:
    return [screener for screener in screeners if screener.name == name][0]


class TestScreeners:
    def test_today_up(self, screeners: list[Screener]):
        screener = get_screener_by_name(screeners, "today_up")
        expected = "cap_10to,sh_opt_option,sh_price_30to,sh_relvol_1to,ta_change_3to"
        actual = screener.encode()
        assert actual == expected

    def test_today_down(self, screeners: list[Screener]):
        screener = get_screener_by_name(screeners, "today_down")
        expected = "cap_10to,sh_opt_option,sh_price_30to,sh_relvol_1to,ta_change_to-3"
        actual = screener.encode()
        assert actual == expected
        assert actual == expected
