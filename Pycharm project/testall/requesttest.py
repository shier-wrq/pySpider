import requests
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
    }
    url = 'https://www.baidu.com/'
    # 处理url携带的参数：封装到字典中
    keyw = input('enter a word:')
    param = {
        'query': keyw
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    """
    print(page_text)
    """
    
    fileName = keyw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功')