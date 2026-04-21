import requests
import pandas as pd
from datetime import datetime

class AgenticVNStock:
    """
    Công cụ lấy dữ liệu tài chính không phụ thuộc thư viện bên thứ 3 (vnstock).
    Sử dụng trực tiếp các Public API (Entrade/DNSE, Vietcap, SSI...)
    """
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive'
        }

    # -------------------------------------------------------------------------
    # 1. CỔ PHIẾU (Giá, Thông tin, Tài chính)
    # -------------------------------------------------------------------------
    def get_stock_historical(self, ticker: str, start: str, end: str) -> pd.DataFrame:
        """Lấy giá lịch sử cổ phiếu (Sử dụng Entrade API)"""
        try:
            start_ts = int(datetime.strptime(start, "%Y-%m-%d").timestamp())
            end_ts = int(datetime.strptime(end, "%Y-%m-%d").timestamp())
            url = f"https://services.entrade.com.vn/chart-api/v2/ohlcs/stock?resolution=1D&symbol={ticker}&from={start_ts}&to={end_ts}"
            
            res = requests.get(url, headers=self.headers, timeout=10)
            if res.status_code == 200:
                data = res.json()
                if data and data.get('t'):
                    df = pd.DataFrame({
                        'Date': pd.to_datetime(data['t'], unit='s').tz_localize('UTC').tz_convert('Asia/Ho_Chi_Minh').strftime('%Y-%m-%d'),
                        'Open': data['o'],
                        'High': data['h'],
                        'Low': data['l'],
                        'Close': data['c'],
                        'Volume': data['v']
                    })
                    return df.sort_values('Date').reset_index(drop=True)
            return pd.DataFrame()
        except Exception:
            return pd.DataFrame()

    def get_company_overview(self, ticker: str) -> pd.DataFrame:
        """Lấy thông tin tổng quan doanh nghiệp (TCBS API)"""
        try:
            url = f"https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/{ticker}/overview"
            res = requests.get(url, headers=self.headers, timeout=10)
            if res.status_code == 200:
                data = res.json()
                if isinstance(data, list) and len(data) > 0:
                    return pd.DataFrame(data)
                elif isinstance(data, dict) and data:
                    return pd.DataFrame([data])
            return pd.DataFrame()
        except Exception:
            return pd.DataFrame()

    def get_financial_ratio(self, ticker: str) -> pd.DataFrame:
        """Lấy chỉ số tài chính (Ví dụ gọi SSI API - Cần cấu trúc chính xác)"""
        try:
            # Ví dụ giả lập / endpoint SSI public:
            url = f"https://fiin-fundamental.ssi.com.vn/FinancialAnalysis/GetFinancialRatio?language=vi&Ticker={ticker}"
            res = requests.get(url, headers=self.headers, timeout=10)
            if res.status_code == 200:
                data = res.json()
                if 'items' in data:
                    return pd.DataFrame(data['items'])
            return pd.DataFrame()
        except Exception:
            return pd.DataFrame()

    # -------------------------------------------------------------------------
    # 2. CHỈ SỐ THỊ TRƯỜNG (VNIndex, HNX, v.v.)
    # -------------------------------------------------------------------------
    def get_market_index(self, index_symbol: str, start: str, end: str) -> pd.DataFrame:
        """
        Lấy dữ liệu chỉ số thị trường.
        Với Entrade: VNINDEX, HNX, UPCOM...
        """
        return self.get_stock_historical(ticker=index_symbol, start=start, end=end)

    # -------------------------------------------------------------------------
    # 3. HỢP ĐỒNG TƯƠNG LAI & 4. CHỨNG QUYỀN
    # -------------------------------------------------------------------------
    def get_derivative_or_cw(self, symbol: str, start: str, end: str) -> pd.DataFrame:
        """Lấy dữ liệu phái sinh (VN30F1M) hoặc Chứng quyền (CHPG2301)"""
        return self.get_stock_historical(ticker=symbol, start=start, end=end)

    # -------------------------------------------------------------------------
    # 5. QUỸ ĐẦU TƯ (ETF & Quỹ mở)
    # -------------------------------------------------------------------------
    def get_fund_data(self) -> pd.DataFrame:
        """Lấy danh sách các Quỹ mở / ETF (Từ Fmarket)"""
        try:
            url = "https://api.fmarket.vn/res/products/filter"
            payload = {"types":["NEW_FUND","TRADING_FUND"],"isWithDividend":True}
            res = requests.post(url, json=payload, headers=self.headers, timeout=10)
            if res.status_code == 200:
                data = res.json()
                if 'data' in data and 'rows' in data['data']:
                    return pd.DataFrame(data['data']['rows'])
            return pd.DataFrame()
        except Exception:
            return pd.DataFrame()

    # -------------------------------------------------------------------------
    # 6. TRÁI PHIẾU
    # -------------------------------------------------------------------------
    def get_bond_data(self) -> pd.DataFrame:
        """Lấy thông tin trái phiếu (Sẽ cần API chuyên biệt như HNX hoặc TCBS Bonds)"""
        # Placeholder cho code tự build
        return pd.DataFrame()

    # -------------------------------------------------------------------------
    # 8. BÁO CÁO TÀI CHÍNH (Kết quả kinh doanh, Bảng cân đối, Lưu chuyển tiền tệ)
    # -------------------------------------------------------------------------
    def get_financial_report(self, ticker: str, report_type: str = "IncomeStatement", period: str = "Quarterly") -> pd.DataFrame:
        """
        Lấy báo cáo tài chính (Cần thay API thực tế từ Vietcap, SSI hoặc DNSE)
        report_type: 'IncomeStatement' (KQKD), 'BalanceSheet' (Bảng CĐKT), 'CashFlow' (LCTT)
        period: 'Quarterly' (Theo quý), 'Yearly' (Theo năm)
        """
        try:
            # Ví dụ dùng API của Vietcap (giả lập cấu trúc thực tế)
            url = f"https://mt.vietcap.com.vn/api/finance/reports?symbol={ticker}&type={report_type}&period={period}"
            res = requests.get(url, headers=self.headers, timeout=10, verify=False)
            if res.status_code == 200:
                data = res.json()
                if isinstance(data, list):
                    return pd.DataFrame(data)
            return pd.DataFrame()
        except Exception:
            return pd.DataFrame()
    def get_company_news(self, ticker: str) -> pd.DataFrame:
        """Lấy tin tức doanh nghiệp (VNDirect API)"""
        try:
            url = f"https://finfo-api.vndirect.com.vn/v4/news?q=symbols:{ticker}&size=15"
            res = requests.get(url, headers=self.headers, timeout=10)
            if res.status_code == 200:
                data = res.json()
                if 'data' in data and isinstance(data['data'], list):
                    return pd.DataFrame(data['data'])
            return pd.DataFrame()
        except Exception:
            return pd.DataFrame()
