import requests
res = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/company/HPG/overview')
print("TCBS overview:", res.status_code)
res_news = requests.get('https://apipubaws.tcbs.com.vn/tcanalysis/v1/ticker/HPG/activity-news')
print("TCBS news:", res_news.status_code)
res_news2 = requests.get('https://finfo-api.vndirect.com.vn/v4/news?q=symbols:HPG&size=10', headers={'User-Agent': 'Mozilla/5.0'})
print("VND news:", res_news2.status_code)
if res_news2.status_code == 200:
    print("VND count:", len(res_news2.json().get('data', [])))
else:
    print(res_news2.text[:100])
