from bs4 import BeautifulSoup

with open("website.html",mode="r") as data:
    contents=data.read()

soup=BeautifulSoup(contents,"html.parser")
print(soup.title)
print(soup.title.string)
all_anchor_tags=soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading=soup.find(name="h1",id="name")
print(heading)

section_heading=soup.find(name="h3",class_="heading")
print(section_heading.getText())

#Using CSS Selector
company_url=soup.select_one(selector="p a")
print(company_url.getText())


headings=soup.select(selector=".heading")
print(headings)
