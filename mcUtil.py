import requests

# 获取鸣潮表单
def mingchaoTable(token):
    url = "http://api.kurobbs.com/gamer/widget/game3/getData"
    headers = {
        "source": "android",
        "Cookie": f"user_token={token}",
        "Accept-Encoding": "gzip",
        "token": token
    }
    data = {
        "type": "1",
        "sizeType": "2"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.text

# 获取鸣潮刷新
def mingchaoRefresh(token):
    mingchaoTable(token)
    url = "http://api.kurobbs.com/gamer/widget/game3/refresh"
    headers = {
        "source": "android",
        "Cookie": f"user_token={token}",
        "Accept-Encoding": "gzip",
        "token": token
    }
    data = {
        "type": "1",
        "sizeType": "2"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.text

def serverSwich(token, devCode):
    url = "http://api.kurobbs.com/config/dict/timingSwitch"
    headers = {
        "version": "2.2.0",
        "devCode": devCode,
        "source": "android",
        "token": token,
        "countryCode": "CN",
        "lang": "zh-Hans",
        "channelId": "2",
        "Cookie": f"user_token={token}"

    }
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.text