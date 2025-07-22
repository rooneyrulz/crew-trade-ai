import yfinance as yf
from crewai.tools import tool

@tool("Live Stock Information Tool")
def get_stock_price(symbol: str) -> str:
    """
    Retrieves the latest stock price and other relevent info for a given stock symbol using Yahoo Finance API.

    Parameters:
    - symbol: The stock symbol to retrieve information for. e.g. AAPL, MSFT, TSLA

    Returns:
    - A string containing the stock's current price, change, and change percentage, the currency it is trading in and other key data.
    """

    ticker = yf.Ticker(symbol)
    info = ticker.info

    current_price = info['regularMarketPrice']
    change = info['regularMarketChange']
    change_percent = info['regularMarketChangePercent']
    currency = info['currency']

    if current_price is None:
        return f"Could not fetch the price for {symbol}"

    return (
        f"Stock: {symbol.upper()}\n"
        f"Price: {current_price} {currency}\n"
        f"Change: {change}\n"
        f"Change %: {change_percent}\n"
        f"Currency: {currency}\n"
    )

# ressult = get_stock_price("TSLA")
# print(ressult)