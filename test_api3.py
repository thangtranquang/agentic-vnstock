import requests
from datetime import datetime

ticker = "HPG"
start_date = "2024-01-01"
end_date = "2024-04-21"
start_ts = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp())
end_ts = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())

url = f"https://apipubaws.tcbs.com.vn/stock-insight/v1/stock/bars?ticker={ticker}&type=stock&resolution=D&from={start_ts}&to={end_ts}"
print(f"URL: {url}")

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'})
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text[:200]}")
