from bs4 import BeautifulSoup
# with open("website.html",encoding="utf8") as file:
#     contents=file.read()
# soup=BeautifulSoup(contents,"html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
# all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))
# # heading =soup.find(name="h1",id="name")
# # print(heading)
# section_heading =soup.find_all("h3",class_="heading")
# print(section_heading)
#
# company_url=soup.select_one(selector="p a")
# print(company_url)
#
# name=soup.select_one(selector="#name")
# print(name)
# headings=soup.select(selector=".heading")
# print(headings)

import requests
response=requests.get("https://news.ycombinator.com/")
yc_webpage=response.text
soup=BeautifulSoup(yc_webpage,"html.parser")
print(soup.title)
articles=soup.find_all(name="a",class_="titlelink")
article_text=[text.getText() for text in articles]
article_link=[article.get("href") for article in articles]
article_upvote=[int(score.getText().split()[0])for score in soup.find_all(name="span",class_="score")]
print(article_upvote)
print(article_link)
print(article_text)
index_of_highest_votes=article_upvote.index(max(article_upvote))
print(article_text[index_of_highest_votes],print(article_text[index_of_highest_votes]))