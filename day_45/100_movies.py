from bs4 import BeautifulSoup
import requests

response=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage=response.text
soup=BeautifulSoup(empire_webpage,"html.parser")
movie_titles=soup.find(name="h3")
print(movie_titles)