import requests
from bs4 import BeautifulSoup

target_url = "https://www.dmzj.com/info/yaoshenji.html"
r = requests.get(url=target_url)
bs = BeautifulSoup(r.text, 'html.parser')
list_con_li = bs.find('ul', class_ = "list_con_li")
comic_list = list_con_li.find_all('a')
chapter_names = []
chapter_urls = []
for comic in comic_list:
    href = comic.get('href')
    name = comic.text
    chapter_names.insert(0, name)
    chapter_urls.insert(0, href)

print(chapter_names)
print(chapter_urls)