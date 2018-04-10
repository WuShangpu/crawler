# -*- coding:utf-8 -*-

import urllib.request as urlrequest
import json

id_list = [26387939, 4920389, 20435622]

for id in id_list:
    url_visit = 'https://api.douban.com/v2/movie/subject/{}'.format(id)
    crawl_content = urlrequest.urlopen(url_visit).read()
    #print(crawl_content.decode('unicode-escape'))

    json_content = json.loads(crawl_content.decode('utf8'))
    rating = json_content['rating']['average']
    title = json_content['title']
    #print(rating)

    with open('movie_rating_score.txt','a') as outputfile:
        outputfile.write('{} {} {}\n'.format(id, title, rating))
