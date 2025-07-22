# 🤖📈 crew-trade-ai

An AI-powered autonomous stock trading system built using [CrewAI](https://github.com/joaomdmoura/crewAI), featuring multi-agent collaboration, real-time stock analysis with [yFinance](https://pypi.org/project/yfinance/), and intelligent decision-making workflows powered by LLMs.

> Note: This project is only for demo purpose.

---

## 🚀 Features

- 🧠 Multi-agent architecture powered by [CrewAI](https://github.com/joaomdmoura/crewAI)
- 📊 Real-time market data via [yFinance](https://pypi.org/project/yfinance/)
- 🤖 Specialized roles: Data Analyst, Strategy Planner, Risk Manager, Execution Agent
- 🗣️ LLM-driven communication and decisions
- 🧪 Extensible and customizable workflows for any asset or strategy
- 📈 Ideal for research, learning, and simulations of AI-powered trading

---

## 📦 Tech Stack

| Role              | Tech Used                                         |
|-------------------|--------------------------------------------------|
| Backend Logic     | 🐍 Python, [CrewAI](https://github.com/joaomdmoura/crewAI) |
| Data Layer        | [yFinance](https://pypi.org/project/yfinance/) for stock market data |
| LLM Agents        | 🔗 LangChain, 💬 OpenAI / Groq / Local LLMs |
| Task Orchestration| 🛠️ Agentic Workflow via CrewAI |
| Visualization     | 📊 (Planned) Matplotlib / Plotly Dash |

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/crew-trade-ai.git
cd crew-trade-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
