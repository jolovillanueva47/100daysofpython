from bs4 import BeautifulSoup
import requests

response=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage=response.text
soup=BeautifulSoup(empire_webpage,"html.parser")

movie_items=soup.select('.listicle-item')
movie_list=[]
for movie in movie_items:
    movie_list.append(movie.img.get("alt"))
movie_list.reverse()

with open(file="movies.txt",mode="a") as file:
    count=0
    for movie in movie_list:
        count+=1
        file.write(f"{count}) {movie}\n")

