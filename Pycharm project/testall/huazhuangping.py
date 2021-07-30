import requests

if __name__ == "__main__":
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    data = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
    }
    headers = {
        'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv: 87.0) Gecko / 20100101Firefox / 87.0'
    }
    id_list = []
    response = requests.post(url=url, data=data, headers=headers)
    json_ids = response.json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])

    post_url = "http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
    for id in id_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=post_url, data=data, headers=headers)
        print(detail_json)