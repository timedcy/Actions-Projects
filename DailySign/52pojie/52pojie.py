import os
import requests 
from bs4 import BeautifulSoup

COOKIE = os.environ['COOKIE']
SCKEY = os.environ["SCKEY"]

def pushinfo(info,specific):
    headers={   
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MI 9 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2580 MMWEBSDK/200502 Mobile Safari/537.36 MMWEBID/8287 MicroMessenger/7.0.15.1680(0x27000F50) Process/toolsmp WeChat/arm32 NetType/4G Language/zh_CN ABI/arm64',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/tpg,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'X-Requested-With': 'com.tencent.mm'
    }
    requests.session().get("https://sc.ftqq.com/"+SCKEY+".send?text=" + info + "&desp=" + specific,headers=headers)


def main(*args):
    headers={
        'Cookie': COOKIE ,
        'ContentType':'text/html;charset=gbk'
    }
    requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2',headers=headers)
    a=requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2',headers=headers)
    b=BeautifulSoup(a.text,'html.parser')          
    c=b.find('div',id='messagetext').find('p').text

    if "您需要先登录才能继续本操作"  in c: 
        pushinfo("Cookie失效", c)
    elif "恭喜"  in c:
        pushinfo("吾爱破解签到成功",c)
    else:
        pushinfo("吾爱破解签到失败",c)
    print(c)


if __name__ == '__main__':
    main()