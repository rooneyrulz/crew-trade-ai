from crewai import Task
from agents.trader_agent import trader

trade_decision = Task(
    description=(
        "Use live market data and stock performance indicators for {stock} to make a strategic trading decision."
        "Assess key factors such as current price, daily change percentage, volume trends, and recent momentum"
        "Based on your analysis, determine whether to **BUY**, **SELL**, or **HOLD** the stock."
    ),
    expected_output=(
        "A clear and confident trading recommendation (Buy / Sell / Hold), supported by:\n"
        "- Current stock price and daily change\n"
        "- Volume and market activity observation\n"
        "- Sentiment analysis\n"
        "- Justification for the trading action on technical signals or risk-reward outlook"
    ),
    agent=trader
)