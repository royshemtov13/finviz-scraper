<!-- FINVIZ SCRAPER -->
# Finviz-Scraper

Finviz scraper is a repository to extract data from the finviz site.

<!-- GETTING STARTED -->
## Getting Started

## Installation

1. Clone the repo

    ```bash
    git clone https://github.com/royshemtov13/finviz-scraper
    ```

2. install python packages with poetry

    ```bash
    poetry install
    ```

3. Create a .env file in the root folder insert the FINVIZ_USERNAME and FINVIZ_PASSWORD

    ```bash
    FINVIZ_USERNAME="your-username"
    FINVIZ_PASSWORD="your-password"
    ```

Great! You're all set

<!-- USAGE -->
## Usage

The most important thing to understand here is the `screeners.yaml` file inside the config folder.

The example there will show you how to write the config file so that the scraper will understand it and work.

Finviz has tons of options to choose from so to simplify it I made two categories of filters to make it easier and also super customizable to the user which are base filters and custom filters.

`Base filters` are the filters which are non value filters (i.e. the stocks sector).

`Custom filters` are the filters which are value customizable (i.e. the stocks price).

For base filters the value can only be an empty string `""` for the filter to take place.

For custom filters to take place you need to provide `low` and `high` attributes. if you provide a string to one of them it will act as if you didn't provide a value to it.

for example. If for the price filter you provided a low of 30 and an empty string `""` it will take all the stock which are from 30 and upwards and vice versa. Basiclly every custom filter has two attributes low and high and an empty string will represent a yes for the filter.

### Example 1

```yaml
- name: today_up
  filters:
    MARKET_CAP:
      low: 10
      high: ""
    OPTIONABLE: ""
    PRICE:
      low: 30
      high: ""
    RELATIVE_VOLUME:
      low: 1
      high: ""
    CHANGE_UP: 3

```

The screener's name is `today_up` and it will return a screener that will scan all the stock as the following:

* market cap from 10B and upwards
* only optionable stocks
* the stocks price will only be from 30 and upwards
* relative volume will be from 1 and upwards
* and the current change (in percentage) of the stock will be at least 3% and upwards

### Example 2

Now lets say I want to have a stock with the following filters:

* Price over 50 but below 250
* Average volume of at least 500K and upwards
* P/E of at least 10 and upwards
* Market cap of up to 100B

This is the screener that I will need to create for the filters to take place is as follows:

```yaml
- name: my_screener
  filters:
    PRICE:
      low: 50
      high: ""
    AVERAGE_VOLUME:
      low: 500
      high: ""
    MARKET_CAP:
      low: ""
      high: 100
    P_E:
      low: 10
      high: ""
```

### `IMPORTANT NOTES`

1. `All available filters can be found in scraper.models.enums.py with an explanation for each filter`
2. `All numbered value filters can be expressed as floats`
3. `Minus values are valid`
4. `Try not to overlap screeners which can result in the same stocks given twice to the DataFrame`
5. `Try not to overlap values in the filters which can cancel each other`

Now, you can have different filters all together and the program will execute them all at the same time and provide you with the combined ```DataFrame``` as a result.

Now you understand the ```screeners.yaml``` file fully. Go ahead change it to your desire
Now you're all set to play with the data. Go to the ```visualize.ipynb``` file within ```scraper.notebooks.visualize.ipynb``` and there you can first check if everything works for you and there you will be able to play with the data to your needs.

This repo also have a ```main.py``` file that returns the data so you can make this repo a lambda function in aws to get the data anywhere you want.

# Available filters

## Base Filters

Remember each base filter's value needs to be an empty string `""` for the filter to take place.

```bash
# SIGNALS
TOP_GAINERS                # highest % price gain today
TOP_LOSERS                 # highest % price loss today
NEW_HIGH                   # Stocks making 52-week high today
NEW_LOW                    # Stocks making 52-week low today
MOST_VOLATILE              # highest widest high/low trading range today
MOST_ACTIVE                # highest trading volume today
UNUSUAL_VOLUME             # Stocks with unusually high volume today - the highest relative volume ratio
OVERBOUGHT                 # calculated by RSI 14 indicator
OVERSOLD                   # calculated by RSI 14 indicator
DOWNGRADES                 # Stocks downgraded by analysts today
UPGRADES                   # Stocks upgraded by analysts today
EARNINGS_BEFORE            # Companies reporting earnings today, before market open
EARNINGS_AFTER             # Companies reporting earnings today, after market close
RECENT_INSIDER_BUYING      # Stocks with recent insider buying
RECENT_INSIDER_SELLING     # Stocks with recent insider selling
MAJOR_NEWS                 # highest news coverage today

# Chart Patterns
HPROZONTAL_SR
TL_RESISTANCE
TL_SUPPORT
WEDGE
TRIANGLE_ASCENDING
TRIANGLE_DESCENDING
CHANNEL_UP
CHANNEL_DOWN
CHANNEL
HEAD_SHOULDERS
HEAD_SHOULDERS_INVERSE

# ANALYST RECOMMENDATION
ANALYST_STRONG_BUY
ANALYST_BUY_BETTER
ANALYST_BUY
ANALYST_HOLD_BETTER
ANALYST_HOLD
ANALYST_HOLD_WORSE
ANALYST_SELL
ANALYST_SELL_WORSE
ANALYST_STRONG_SELL

# OPTIONABLE / SHORTABLE AND INVERSE
OPTIONABLE
SHORTABLE
NOT_SHORTABLE
OPTIONABLE_SHORTABLE
OPTIONABLE_NOT_SHORTABLE
```

## Custom Filters

Remember each custom filter needs to have a `low` and a `high` and their values can be represented as floats or an empty string `""` if both `low` and `high` are accidently empty strings the filter will not take place.

With the only exceptions being the `EARNINGS_DATE` filter being a date from-to filter in the format `mm-dd-yyyy`

And the `PERFORMANCE` filters which can only take one low or high attributes meaning one or the other has to be an empty string

```bash
# PERCENTAGE VALUES

PRICE_FREE_CASH_FLOW
EPS_GROWTH_THIS_YEAR
EPS_GROWTH_NEXT_YEAR
EPS_GROWTH_PAST_FIVE_YEARS
EPS_GROWTH_NEXT_FIVE_YEARS
SALES_GROWTH_NEXT_FIVE_YEARS
EPS_GROWTH_QTR_OVER_QTR
SALES_GROWTH_QTR_OVER_QTR
DIVIDEND_YIELD
RETURN_ON_ASSETS
RETURN_ON_EQUITY
RETURN_ON_INVESTMENT
GROSS_MARGIN
OPERATING_MARGIN
NET_PROFIT_MARGIN
PAYOUT_RATIO
INSIDER_OWNERSHIP
INSIDER_TRANSACTIOONS
INSTITUTIONAL_OWNERSHIP
INSTITUTIONAL_TRANSACTIONS
FLOAT_SHORT
GAP
CHANGE
CHANGE_FROM_OPEN
AFTER_HOURS_CHANGE

PRICE_ABOVE_SMA_20
PRICE_ABOVE_SMA_50
PRICE_ABOVE_SMA_200
PRICE_BELOW_SMA_20
PRICE_BELOW_SMA_50
PRICE_BELOW_SMA_200

# Numbered Values

PRICE_EARNINGS
FORWARD_P_E
PRICE_EARNINGS_GROWTH
PRICE_SALES
PRICE_BOOK
PRICE_CASH
CURRENT_RATIO
QUICK_RATIO
LT_DEBT_EQUITY
DEBT_EQUITY
RELATIVE_VOLUME
RSI_14
BETA
ATR
PRICE
AFTER_HOURS_CLOSE
MARKET_CAP                      # Represented in BILLIONS
SHARES_OUTSTANDING              # Represented in MILLIONS
AVERAGE_VOLUME                  # Represented in THOUSANDS
CURRENT_VOLUME                  # Represented in THOUSANDS
EARNINGS_DATE                   # FORMAT mm/dd/yyyy low means start and high means end

PERFORMANCE_DAY                 # ONLY LOW OR HIGH NOT BOTH
PERFORMANCE_WEEK                # ONLY LOW OR HIGH NOT BOTH
PERFORMANCE_MONTH               # ONLY LOW OR HIGH NOT BOTH
PERFORMANCE_QUARTER             # ONLY LOW OR HIGH NOT BOTH
PERFORMANCE_HALF                # ONLY LOW OR HIGH NOT BOTH
PERFORMANCE_YTD                 # ONLY LOW OR HIGH NOT BOTH

```

# Columns for the extracted dataframe

All column explanation for the dataframe.
For now this is all the settings available for the scraper in finviz.
The data in the ```DataFrame``` is raw and unchanged.

```bash

ticker                              #  Stock trading symbol
company                             #  Name of the company
index                               #  Stock market index affiliation
sector                              #  Broad industry category
industry                            #  Specific business sector
country                             #  Company's headquarters location
market_cap                          #  Total company value in the market
p_e                                 #  Stock price to earnings ratio
forward_p_e                         #  Expected future P/E ratio
peg                                 #  P/E ratio relative to growth rate
p_s                                 #  Market cap to annual sales ratio
p_b                                 #  Stock price to book value ratio
p_cash                              #  Stock price to cash per share ratio
p_free_cash_flow                    #  Stock price to free cash flow per share ratio
book_sh                             #  Shareholder equity per share
cash_sh                             #  Total cash per share
dividend                            #  Distribution of company profits to shareholders
dividend_yield                      #  Ratio of annual dividends to stock price
payout_ratio                        #  Proportion of earnings paid as dividends
eps_ttm                             #  Company's net earnings per share
eps_next_q                          #  Expected EPS for the next quarter
eps_growth_this_year                #  Projected EPS growth for the current year
eps_growth_next_year                #  Projected EPS growth for the next year
eps_growth_past_5_years             #  Average EPS growth over 5 years
eps_growth_next_5_years             #  Projected EPS growth for 5 years
sales_growth_past_5_years           #  Average sales growth over 5 years
sales_growth_quarter_over_quarter   #  Sales growth between quarters
eps_growth_quarter_over_quarter     #  EPS growth between quarters
sales                               #  Total revenue generated
income                              #  Net profit or earnings
shares_outstanding                  #  Total issued shares
shares_float                        #  Tradable shares in the market
float                               #  Percentage of tradable shares
insider_ownership                   #  Percentage of shares held by insiders
insider_transactions                #  Insider share transactions
institutional_ownership             #  Percentage of shares held by institutions
institutional_transactions          #  Institutional share transactions
float_short                         #  Shorted shares
short_ratio                         #  Ratio of shorted shares to average volume
short_interest                      #  Percentage of shorted shares
return_on_assets                    #  Efficiency of asset utilization
return_on_equity                    #  Profitability relative to equity
return_on_investment                #  Efficiency of investments
current_ratio                       #  Current assets to liabilities ratio
quick_ratio                         #  Immediate liquidity ratio
lt_debt_equity                      #  Long term debt to equity ratio
total_debt_equity                   #  Total debt to equity ratio
gross_margin                        #  Revenue minus cost of goods sold ratio
operating_margin                    #  Operating income as a percentage of revenue
profit_margin                       #  Net profit as a percentage of revenue
performance_week                    #  Weekly stock price change percentage
performance_month                   #  Monthly stock price change percentage
performance_quarter                 #  Quarterly stock price change percentage
performance_half_year               #  6 month stock price change percentage
performance_year                    #  Yearly stock price change percentage
performance_ytd                     #  Year to date stock price change percentage
beta                                #  Measure of stock volatility
average_true_range                  #  Stock price volatility measure
volatility_week                     #  Weekly stock price variability
volatility_month                    #  Monthly stock price variability
20_day_simple_moving_average        #  Average price over 20 days
50_day_simple_moving_average        #  Average price over 50 days
200_day_simple_moving_average       #  Average price over 200 days
50_day_high                         #  Highest price in the last 50 days
50_day_low                          #  Lowest price in the last 50 days
52_week_high                        #  Highest price in the last 52 weeks
52_week_low                         #  Lowest price in the last 52 weeks
relative_strength_index_14          #  Momentum indicator
earnings_date                       #  Scheduled earnings release date
ipo_date                            #  Initial public offering date
optionable                          #  Availability of options for trading
shortable                           #  Ability to short sell the stock
employees                           #  Company workforce count
change_from_open                    #  Difference between open and current price
gap                                 #  Difference between previous close and current open
analyst_recom                       #  Analysts' consensus recommendation
average_volume                      #  Average shares traded
relative_volume                     #  Current volume compared to average
volume                              #  Total shares traded
target_price                        #  Estimated future stock price
prev_close                          #  Last closing price
open                                #  Opening price
high                                #  Highest price in a period
low                                 #  Lowest price in a period
price                               #  Current price
change                              #  Price change from the previous day
after_hours_close                   #  Closing price after regular trading hours
after_hours_change                  #  Price change after regular trading hours
```
