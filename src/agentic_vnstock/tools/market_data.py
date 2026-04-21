# File này chứa các tool để Agent gọi lấy data (Wrap lại từ client.py)
from ..client import AgenticVNStock

def get_stock_price_tool(ticker: str, start_date: str, end_date: str) -> str:
    """Tool cho AI Agent lấy giá cổ phiếu."""
    client = AgenticVNStock()
    df = client.get_historical_price(ticker, start_date, end_date)
    if df.empty:
        return f"Không tìm thấy dữ liệu cho {ticker}."
    return df.to_string()
