from crewai import Crew 

from agents.analyst_agent import analyst
from agents.trader_agent import trader
from tasks.analyze_task import get_stock_analysis
from tasks.trade_task import trade_decision

stock_crew = Crew(
    agents=[analyst, trader],
    tasks=[get_stock_analysis, trade_decision],
    verbose=True
)