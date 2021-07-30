from lxml import etree
import requests
if __name__ == "__main__":
    url = 'https://bj.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
    }
    page_text = requests.get(url=url, headers=headers).text
    #数据解析
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)