# agentic-vnstock

A lightweight, zero-bloat library to fetch Vietnam stock market data, perfectly designed for AI Agents, LLMs, and Data Analysts.

## Features (Phase 1)
- Fetch historical stock prices (OHLCV) for any ticker on HOSE, HNX, and UPCOM.
- Output clean, ready-to-use Pandas DataFrames or CSV files.
- Zero dependencies on bloated third-party charting libraries; uses only `requests` and `pandas`.
- Built-in CLI for instant data extraction without writing Python code.

## Installation
```bash
pip install agentic-vnstock
```

## Quick CLI Usage
You can use the built-in command-line interface to quickly download stock data to a CSV file. The basic syntax is:
```bash
agentic-vnstock stock <TICKER> <START_DATE> <END_DATE>
```

**Example: Fetch FPT stock data for the first half of 2026:**
```bash
agentic-vnstock stock FPT 2026-01-01 2026-06-30
```
This will create a file named `FPT_data.csv` in your current directory containing Date, Open, High, Low, Close, and Volume.

*(Note: If you are on Windows and get a "command not found" error because your Python Scripts folder isn't in your PATH, you can always run it via Python directly:)*
```bash
python -m agentic_vnstock.cli stock FPT 2026-01-01 2026-06-30
```

## Python Usage
Use it directly in your Python scripts, Jupyter Notebooks, or AI Agent tools.

```python
from agentic_vnstock import AgenticVNStock

client = AgenticVNStock()

# Fetch historical price data for HPG from Jan 1, 2026 to Apr 21, 2026
df = client.get_historical_price("HPG", "2026-01-01", "2026-04-21")
print(df.head())
```

## Architecture Roadmap
- **Phase 1 (Current):** Blazing fast data fetching from TCBS APIs (`client.py`) and easy CLI export.
- **Phase 2 (Upcoming):** Built-in AI Agents (`agents/`) and Tools (`tools/`) optimized for LLM integrations (LangChain, LlamaIndex, OpenAI function calling).
