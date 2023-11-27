from scraper.models.enums import FilterCodes
from scraper.models.screener import Screener


class TestScreeners:
    def test_config_filters(self):
        filters = {
            "MARKET_CAP": {"low": 10, "high": ""},
            "OPTIONABLE": "",
            "PRICE": {"low": 50, "high": ""},
            "RELATIVE_VOLUME": {"low": 1, "high": ""},
            "CHANGE": {"low": 3, "high": ""},
        }

        screener = Screener(name="custom", filters=filters)
        expected = "cap_10to,sh_opt_option,sh_price_50to,sh_relvol_1to,ta_change_3to"
        actual = screener.encode()
        assert actual == expected

    def test_custom_filters(self):
        filters = {
            "MARKET_CAP": {"low": 1, "high": 10},
            "PRICE_EARNINGS": {"low": 1, "high": 10},
            "FORWARD_P_E": {"low": 1, "high": 10},
            "PRICE_EARNINGS_GROWTH": {"low": 1, "high": 10},
            "PRICE_SALES": {"low": 1, "high": 10},
            "PRICE_BOOK": {"low": 1, "high": 10},
            "PRICE_CASH": {"low": 1, "high": 10},
            "PRICE_FREE_CASH_FLOW": {"low": 1, "high": 10},
            "EPS_GROWTH_THIS_YEAR": {"low": 1, "high": 10},
            "EPS_GROWTH_NEXT_YEAR": {"low": 1, "high": 10},
            "EPS_GROWTH_PAST_FIVE_YEARS": {"low": 1, "high": 10},
            "EPS_GROWTH_NEXT_FIVE_YEARS": {"low": 1, "high": 10},
            "SALES_GROWTH_NEXT_FIVE_YEARS": {"low": 1, "high": 10},
            "EPS_GROWTH_QTR_OVER_QTR": {"low": 1, "high": 10},
            "SALES_GROWTH_QTR_OVER_QTR": {"low": 1, "high": 10},
            "DIVIDEND_YIELD": {"low": 1, "high": 10},
            "RETURN_ON_ASSETS": {"low": 1, "high": 10},
            "RETURN_ON_EQUITY": {"low": 1, "high": 10},
            "RETURN_ON_INVESTMENT": {"low": 1, "high": 10},
            "CURRENT_RATIO": {"low": 1, "high": 10},
            "QUICK_RATIO": {"low": 1, "high": 10},
            "LT_DEBT_EQUITY": {"low": 1, "high": 10},
            "DEBT_EQUITY": {"low": 1, "high": 10},
            "GROSS_MARGIN": {"low": 1, "high": 10},
            "OPERATING_MARGIN": {"low": 1, "high": 10},
            "NET_PROFIT_MARGIN": {"low": 1, "high": 10},
            "PAYOUT_RATIO": {"low": 1, "high": 10},
            "INSIDER_OWNERSHIP": {"low": 1, "high": 10},
            "INSIDER_TRANSACTIOONS": {"low": 1, "high": 10},
            "INSTITUTIONAL_OWNERSHIP": {"low": 1, "high": 10},
            "INSTITUTIONAL_TRANSACTIONS": {"low": 1, "high": 10},
            "FLOAT_SHORT": {"low": 1, "high": 10},
            "RSI_14": {"low": 1, "high": 10},
            "GAP": {"low": 1, "high": 10},
            "CHANGE": {"low": 1, "high": 10},
            "CHANGE_FROM_OPEN": {"low": 1, "high": 10},
            "BETA": {"low": 1, "high": 10},
            "ATR": {"low": 1, "high": 10},
            "AVERAGE_VOLUME": {"low": 1, "high": 10},
            "RELATIVE_VOLUME": {"low": 1, "high": 10},
            "CURRENT_VOLUME": {"low": 1, "high": 10},
            "PRICE": {"low": 1, "high": 10},
            "SHARES_OUTSTANDING": {"low": 1, "high": 10},
            "AFTER_HOURS_CLOSE": {"low": 1, "high": 10},
            "AFTER_HOURS_CHANGE": {"low": 1, "high": 10},
            "PERFORMANCE_DAY": {"low": 1, "high": 10},
            "PERFORMANCE_WEEK": {"low": 1, "high": 10},
            "PERFORMANCE_MONTH": {"low": 1, "high": 10},
            "PERFORMANCE_QUARTER": {"low": 1, "high": 10},
            "PERFORMANCE_HALF": {"low": 1, "high": 10},
            "PERFORMANCE_YTD": {"low": 1, "high": 10},
            "PRICE_ABOVE_SMA_20": {"low": 1, "high": 10},
            "PRICE_ABOVE_SMA_50": {"low": 1, "high": 10},
            "PRICE_ABOVE_SMA_200": {"low": 1, "high": 10},
            "PRICE_BELOW_SMA_20": {"low": 1, "high": 10},
            "PRICE_BELOW_SMA_50": {"low": 1, "high": 10},
            "PRICE_BELOW_SMA_200": {"low": 1, "high": 10},
        }
        screener = Screener(name="custom", filters=filters)
        encoded_filters = [
            FilterCodes[key].value.replace("to", f"{value['low']}to{value['high']}")
            for key, value in filters.items()
        ]
        expected = ",".join(encoded_filters)

        actual = screener.encode()
        assert actual == expected

    def test_base_encodings(self):
        filters = {
            "TOP_GAINERS": "",
            "TOP_LOSERS": "",
            "NEW_HIGH": "",
            "NEW_LOW": "",
            "MOST_VOLATILE": "",
            "MOST_ACTIVE": "",
            "UNUSUAL_VOLUME": "",
            "OVERBOUGHT": "",
            "OVERSOLD": "",
            "DOWNGRADES": "",
            "UPGRADES": "",
            "EARNINGS_BEFORE": "",
            "EARNINGS_AFTER": "",
            "RECENT_INSIDER_BUYING": "",
            "RECENT_INSIDER_SELLING": "",
            "MAJOR_NEWS": "",
            "HPROZONTAL_SR": "",
            "TL_RESISTANCE": "",
            "TL_SUPPORT": "",
            "WEDGE": "",
            "TRIANGLE_ASCENDING": "",
            "TRIANGLE_DESCENDING": "",
            "CHANNEL_UP": "",
            "CHANNEL_DOWN": "",
            "CHANNEL": "",
            "HEAD_SHOULDERS": "",
            "HEAD_SHOULDERS_INVERSE": "",
            "ANALYST_STRONG_BUY": "",
            "ANALYST_BUY_BETTER": "",
            "ANALYST_BUY": "",
            "ANALYST_HOLD_BETTER": "",
            "ANALYST_HOLD": "",
            "ANALYST_HOLD_WORSE": "",
            "ANALYST_SELL": "",
            "ANALYST_SELL_WORSE": "",
            "ANALYST_STRONG_SELL": "",
            "OPTIONABLE": "",
            "SHORTABLE": "",
            "NOT_SHORTABLE": "",
            "OPTIONABLE_SHORTABLE": "",
            "OPTIONABLE_NOT_SHORTABLE": "",
        }

        screener = Screener(name="base", filters=filters)
        expected = ",".join([FilterCodes[key].value for key in filters])
        actual = screener.encode()
        assert actual == expected

    def test_date_encoding(self):
        screener = Screener(
            name="date",
            filters={
                "EARNINGS_DATE": {"low": "11-22-2023", "high": ""},
            },
        )
        expected = "earningsdate_11-22-2023x"
        actual = screener.encode()
        assert actual == expected
