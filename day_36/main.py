import os, requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_API_KEY=os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
account_sid = "AC67ae3cf0843b0ea8ebc3641014efb472"
auth_token =os.environ.get("TWILIO_AUTH_TOKEN")

alpha_vantage_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "outputsize":"compact",
    "apikey":ALPHA_API_KEY
}

news_params={
    "q":COMPANY_NAME,
    "apikey":NEWS_API_KEY
}

response=requests.get(STOCK_ENDPOINT, params=alpha_vantage_params)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]
yesterday_date=list(data.keys())[0]
yesterday_closing_price=data[yesterday_date]["4. close"]

day_before_yesterday_date=list(data.keys())[1]
day_before_yesterday_closing_price=data[day_before_yesterday_date]["4. close"]


difference=float(yesterday_closing_price)-float(day_before_yesterday_closing_price)
abs_difference=abs(difference)

if difference > 0:
    symbol="🔺"
else:
    symbol="🔻"
percentage_diff=(abs_difference/float(yesterday_closing_price))*100


if percentage_diff > 5:
    print("Get News")
    news_response=requests.get(NEWS_ENDPOINT, params=news_params)
    news_data=news_response.json()["articles"][:3]
    # print(news_data)
    filtered_news_dict={item["title"]:item["description"] for item in news_data}
    client = Client(account_sid, auth_token)
    for key,value in filtered_news_dict.items():
        stock_msg=f"{STOCK_NAME}: {symbol}{percentage_diff}%\n"
        news_msg=f"Headlines: {key}\nBrief:{value}\n"
        message = client.messages.create(
        from_="+13203346108",
        to="+639760126997",
        body=stock_msg+news_msg)
        print(message.status)


