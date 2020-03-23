
import requests
from faker import Faker
from lxml import etree

def thessr():
  ## 1.注册
  fake = Faker()
  email = fake.email()
  name = fake.user_name()
  passwd = str(fake.random_number(digits=10))
  wechat = str(fake.random_number(digits=10))

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

  thessr_session = requests.Session()
  thessr_session.headers=headers

  data = {
    'email': email,
    'name': name,
    'passwd': passwd,
    'repasswd': passwd,
    'wechat': wechat,
    'imtype': '2',
    'code': '0'
  }

  response = thessr_session.post('https://thessr.cn/auth/register', headers=headers, data=data)
  msg=response.json()

  ## print(msg)
  ## 2.登录/获取链接

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

  thessr_session.headers.update(headers)
  data = {
    'email': email,
    'passwd': passwd,
    'code': ''
  }

  thessr_session.post('https://thessr.cn/auth/login', headers=headers, data=data)
  response = thessr_session.get('https://thessr.cn/user')
  selector = etree.HTML(response.text)
  ssr = selector.xpath(r"//div[@id='all_ssr']//input[@name='input1']/@value")[0]
  return ssr

if __name__ == "__main__":
    ssr = thessr()
    print(ssr)