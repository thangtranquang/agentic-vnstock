# agentic-vnstock

A lightweight, zero-bloat library to fetch Vietnam stock market data, perfectly designed for AI Agents, LLMs, and Data Analysts.

## Architecture
- **Phase 1 (Current):** Blazing fast data fetching from TCBS (`client.py`) and easy CLI export.
- **Phase 2 (Upcoming):** Built-in AI Agents (`agents/`) and Tools (`tools/`) for LLM integrations (LangChain, LlamaIndex, OpenAI function calling).

## Installation
```bash
pip install agentic-vnstock
```

## Quick CLI Usage (Phase 1)
Download CSV data instantly from your terminal:
```bash
agentic-vnstock FPT 2024-01-01 2024-04-21
```

## Python Usage (Phase 1)
```python
from agentic_vnstock import AgenticVNStock

client = AgenticVNStock()
df = client.get_historical_price("FPT", "2024-01-01", "2024-04-21")
print(df.head())
```
