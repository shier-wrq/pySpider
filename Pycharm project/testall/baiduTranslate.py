import requests

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
    }
    word = input('enter a word:')
    data = {
        'kw': word
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    dic_obj = response.json()
    print(dic_obj)