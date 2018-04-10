# -*- coding:utf-8 -*-


from bs4 import BeautifulSoup
import urllib.request as urlrequest

movie_url = 'https://movie.douban.com/subject/26387939/'
url_visit = urlrequest.urlopen(movie_url).read()
#print(url_visit)

soup = BeautifulSoup(url_visit, 'html.parser')
#print(soup.prettify())

rating = soup.find(class_='ll rating_num').get_text()
print(rating)
