

import requests

cookies = {
    '__cfduid': 'd0606fab38d8aa8acd4900d36e6b71a931589706914',
    'PHPSESSID': '871g6d07ndgm6paf2l314m1q2n',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.viyundingji.xyz',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.viyundingji.xyz/auth/register',
    'TE': 'Trailers',
}

data = {
  'email': '99999999@gmail.com',
  'name': '99999999',
  'passwd': '99999999',
  'repasswd': '99999999',
  'code': '0',
  'geetest_challenge': '7985bbb117de9e00aa25c330e783a22bd9',
  'geetest_validate': '261e881d7c7e9fb830d09f69b02528ab',
  'geetest_seccode': '261e881d7c7e9fb830d09f69b02528ab|jordan'
}

response = requests.post('https://www.viyundingji.xyz/auth/register', headers=headers, cookies=cookies, data=data)
