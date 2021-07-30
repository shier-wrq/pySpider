import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}
play_url = 'http://music.163.com/playlist?id=5041773022' \
           ''

s = requests.session()
response = s.get(play_url, headers=headers).content
s = BeautifulSoup(response, 'html.parser')
main = s.find('ul', {'class': 'f-hide'})

lists = []
for music in main.find_all('a'):
    print('{} : {}'.format(music.text, music['href']))
"""
    listr = []
    musicUrl = 'http://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'
    musicName = music.text
    listr.append(musicName)
    listr.append(musicUrl)
    lists.append(listr)


print(lists)

for i in lists:
    url = i[1]
    name = i[0]
    try:
        print('loading', name)
        urllib.request.urlretrieve(url, './music/%s.mp3' % name)
        print('Successful')
    except:
        print('failed')
"""