from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
yc_webpage=response.text
soup=BeautifulSoup(yc_webpage,"html.parser")
articles=soup.select(selector=".storylink")
article_texts=[]
article_links=[]
for article_tag in articles:
    article_text=article_tag.getText()
    article_texts.append(article_text)
    article_link=article_tag.get("href")
    article_links.append(article_link)

#print(article_texts)
#print(article_links)

article_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]
print(article_upvotes)
highest_pts=max(article_upvotes)
index=article_upvotes.index(highest_pts)
print(article_texts[index+1])
print(article_links[index+1])
