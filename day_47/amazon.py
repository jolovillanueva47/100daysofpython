import requests
from bs4 import BeautifulSoup


amazon_url="https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

amz_headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Accept-Language":"en-US,en;q=0.5"
}

response=requests.get(amazon_url,headers=amz_headers)

print(response.text)