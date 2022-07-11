from bs4 import BeautifulSoup
import requests
response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/bes"
                      "t-movies-2/")
best_movies=response.text

soup=BeautifulSoup(best_movies,features="html.parser")
movies=[movie.getText() for movie in soup.find_all(name="h3",class_="title")]
sorted_movies=movies[::-1]

with open ("movies.txt",mode="w",encoding="utf8") as file:
    for movie in sorted_movies:
        file.write(f"{movie}\n")

