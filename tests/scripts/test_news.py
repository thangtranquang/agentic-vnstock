import requests
headers = {'User-Agent': 'Mozilla/5.0'}
# Test TCBS info
r_info = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/HPG/overview', headers=headers)
print("TCBS Info:", r_info.status_code)
if r_info.status_code == 200: print(r_info.json().keys())

# Test VNDirect news
url_vnd = 'https://finfo-api.vndirect.com.vn/v4/news?q=symbols:HPG&size=5'
r_news = requests.get(url_vnd, headers=headers)
print("VND News:", r_news.status_code)
if r_news.status_code == 200 and 'data' in r_news.json() and r_news.json()['data']:
    print(r_news.json()['data'][0]['publishDate'], r_news.json()['data'][0]['title'])
else:
    # Try FireAnt news
    url_fa = 'https://restv2.fireant.vn/symbols/HPG/news?offset=0&limit=5'
    r_fa = requests.get(url_fa, headers=headers)
    print("FireAnt News:", r_fa.status_code)
    if r_fa.status_code == 200 and len(r_fa.json()) > 0:
        print(r_fa.json()[0].get('title'))
