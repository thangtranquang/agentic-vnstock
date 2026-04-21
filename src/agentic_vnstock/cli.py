import argparse
import sys
from .client import AgenticVNStock

def main():
    parser = argparse.ArgumentParser(description="Công cụ tải dữ liệu tài chính Việt Nam toàn diện cho AI Agents.")
    subparsers = parser.add_subparsers(dest="command", help="Danh mục tính năng")

    # 1. Cổ phiếu
    stock_parser = subparsers.add_parser("stock", help="Lấy dữ liệu lịch sử giá cổ phiếu")
    stock_parser.add_argument("ticker", help="Mã (VD: HPG)")
    stock_parser.add_argument("start", help="Ngày bắt đầu (YYYY-MM-DD)")
    stock_parser.add_argument("end", help="Ngày kết thúc (YYYY-MM-DD)")

    # Thông tin công ty
    info_parser = subparsers.add_parser("info", help="Lấy thông tin tổng quan doanh nghiệp")
    info_parser.add_argument("ticker", help="Mã (VD: HPG)")

    # Tin tức
    news_parser = subparsers.add_parser("news", help="Lấy tin tức sự kiện của doanh nghiệp")
    news_parser.add_argument("ticker", help="Mã (VD: HPG)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        client = AgenticVNStock()
        
        if args.command == "stock":
            print(f"📥 Đang tải dữ liệu {args.ticker} từ {args.start} đến {args.end}...")
            df = client.get_stock_historical(args.ticker, args.start, args.end)
            if not df.empty:
                filename = f"{args.ticker}_history.csv"
                df.to_csv(filename, index=False)
                print(f"✅ Đã lưu: {filename}")
            else:
                print("❌ Không có dữ liệu.")

        elif args.command == "info":
            print(f"📥 Đang tải thông tin {args.ticker}...")
            df = client.get_company_overview(args.ticker)
            if not df.empty:
                filename = f"{args.ticker}_info.csv"
                df.to_csv(filename, index=False)
                print(f"✅ Đã lưu: {filename}")
            else:
                print("❌ Không có dữ liệu.")

        elif args.command == "news":
            print(f"📥 Đang tải tin tức {args.ticker}...")
            df = client.get_company_news(args.ticker)
            if not df.empty:
                filename = f"{args.ticker}_news.csv"
                df.to_csv(filename, index=False)
                print(f"✅ Đã lưu: {filename}")
            else:
                print("❌ Không có dữ liệu.")

    except Exception as e:
        print(f"❌ Lỗi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()