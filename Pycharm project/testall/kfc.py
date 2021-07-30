import requests

if __name__ == "__main__":
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
    }
    pos = input('enter a position:')
    pageIndex = input('enter a page:')
    data = {
        "cname": "",
        "pid": "",
        "keyword": pos,
        "pageIndex": pageIndex,
        "pageSize": "10"
    }
    response = requests.post(url=post_url, headers=headers, data=data)
    kfc_text = response.text
    print(kfc_text)  