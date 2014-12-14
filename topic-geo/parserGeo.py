import json
import nltk
from bs4 import BeautifulSoup

f_in = open('tweets.txt','r')
f_geo = open('geo.txt','w')
for line in f_in.readlines():
    js_data = json.loads(line)
    usr_id = js_data['id']
    if 'geo' in js_data.keys():
        geo = js_data['geo']
    else:
        geo = 'nogeo'
    time = js_data['pub_time']['$date']
    if 'retct' in js_data.keys():
        retct = js_data['retct']
    else:
        retct = 0
    html_data = BeautifulSoup(js_data['content'])
    raw_data = html_data.get_text().replace('\n',' ')
    #print usr_id,raw_data
    if geo != 'nogeo':
        f_geo.write('{0}\t{1}\t{2}\t{3}\t{4}\n'.format(usr_id,geo,time,retct,raw_data.encode('utf-8')))

f_geo.close()
