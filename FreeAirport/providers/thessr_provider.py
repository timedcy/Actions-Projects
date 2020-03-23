
## NOTE: 机场地址 https://thessr.cn

#### 1.注册账号

import requests
from lxml import etree





cookies = {
    '__cfduid': 'da20a7be1f22c1bf7f20360f50a82b78a1584939177',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://thessr.cn',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://thessr.cn/auth/register',
    'TE': 'Trailers',
}

data = {
  'email': 'hahahaha@163.com',
  'name': 'hahahaqqq`',
  'passwd': '12345678',
  'repasswd': '12345678',
  'wechat': '3424234242',
  'imtype': '2',
  'code': '0'
}

response = requests.post('https://thessr.cn/auth/register', headers=headers, cookies=cookies, data=data)



### 登录账号

cookies = {
    '__cfduid': 'da20a7be1f22c1bf7f20360f50a82b78a1584939177',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://thessr.cn',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://thessr.cn/auth/login',
    'TE': 'Trailers',
}

data = {
  'email': 'hahahaha@163.com',
  'passwd': '12345678',
  'code': ''
}

response = requests.post('https://thessr.cn/auth/login', headers=headers, cookies=cookies, data=data)

### 获取订阅链接
def get_ssr():

    response = yuyucool_session.get('https://yuyu.cool/nodeList', headers=headers)
    selector = etree.HTML(response.text)
    ssr = selector.xpath(
        r"//input[@id='subscribe_link']/@value")[0]
    return ssr

def get_v2ray():

    response = yuyucool_session.get('https://yuyu.cool/nodeList', headers=headers)
    selector = etree.HTML(response.text)
    ssr = selector.xpath(
        r"//input[@id='subscribe_link']/@value")[0]
    return ssr