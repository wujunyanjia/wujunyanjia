"""
Project: 86python
Author:柠檬班-Tricy
Time:2021/11/29 20:43
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
"""
'''
使用第三方库两步：
1、安装
2、导入 ： import 

物业接口项目：
url:http://47.115.15.198:7001/smarthome/user/register
参数：{"phone":"17750542236",
"pwd":"1234567a",
"rePwd":"1234567a",
"userName":"柠檬小可爱1",
"verificationCode":"611203"}
请求头：X-Lemonban-Media-Type:lemonban.v2
Content-Type:application/json

'''
import requests  # 导入到Python文件里可以使用  == 针对本个Python有效
import pprint  # prety-print  == 不用安装
import jsonpath  # pip install jsonpath

# 注册
url_wuye ='http://47.115.15.198:7001/smarthome/user/register'  # 地址定义
data_wuye = {"phone":"13656565757",
"pwd":"1234567a",
"rePwd":"1234567a",
"userName":"柠檬86开4",
"verificationCode":"lemon"}
header_wy = {"X-Lemonban-Media-Type":"lemonban.v2",
"Content-Type":"application/json"}

res = requests.post(url=url_wuye,json=data_wuye,headers=header_wy)  # 用一个变量接受返回值
pprint.pprint(res.json())

# 登录
url_login ='http://47.115.15.198:7001/smarthome/user/login'  # 地址定义
data_login = {  "userName": "柠檬86开4",
  "pwd": "1234567a"}
header_login = {"X-Lemonban-Media-Type":"lemonban.v2",
"Content-Type":"application/json"}

res_login = requests.post(url=url_login,json=data_login,headers=header_login)  # 用一个变量接受返回值
res_login = res_login.json()
pprint.pprint(res_login)

'''
res_login = 
{'code': '0',
 'data': {'id': 162565,
          'phone': '13656565757',
          'token_info': {'expires_in': '2021-11-29 21:22:48',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoiMTYyNTY1IiwiZXhwIjoxNjM4MTkyMTY4fQ.uKNuxHEQH11a6JTVp1uKVg9okSwWGQzo7r5TW4d8bn10QtPpkLRZxN6G1zp9hukKNXQYUIAez3LSX0A8UnH66g',
                         'token_type': 'Bearer'},
          'type': False,
          'user_name': '柠檬86开4'},
 'msg': '操作成功'}
'''
# 第一种方式：字典取值
# id = res_login["data"]["id"]
# token = res_login["data"]["token_info"]["token"]
# 第一种方式：jsonpath --高级
id = jsonpath.jsonpath(res_login,"$..id")[0]   # jsonpath 列表 取值   = ..任意层
token = jsonpath.jsonpath(res_login,"$..token")[0]
print(id, token)

# 完善信息
url_ws ='http://47.115.15.198:7001/smarthome/merchant/complete'  # 地址定义
data_ws = {
  "address": "湖南省长沙市岳麓区xx街道12345678901234567",
  "establishDate": "2021-04-02",
  "legalPerson": "韩",
  "licenseCode": "xh430646464sdfa",
  "licenseUrl": "http://127.0.0.1/smarthome/aaa.jpg",
  "merchantName": "青海文梅科技有限公司1234567890",
  "merchantType": 2,
  "registerAuthority": "城中区派出所123456789012345678901234",
  "tel": "18888888888",
  "userId":id ,
  "validityDate": "2033-05-02"
}
header_ws = {"X-Lemonban-Media-Type":"lemonban.v2",
"Content-Type":"application/json","Authorization":"Bearer "+token}

res_ws = requests.put(url=url_ws,json=data_ws,headers=header_ws)  # 用一个变量接受返回值
pprint.pprint(res_ws.json())

# 面试题扩展：请求百度请求做一下 requests怎么发送接口请求？
'''
问题：
1、乱码的问题 == 中文编码
2、 内容不一样  ==随意给你返回页面？
User-Agent
	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0
	没有带上这个头部，百度服务器认为一个爬虫（通过代码工具去获取页面里的一些内容的技术）--反爬机制！
'''
url_baidu = "https://www.baidu.com/"
header_baidu = {"User-Agent":
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"}
res_baidu = requests.get(url=url_baidu,headers=header_baidu)
# print(res_baidu.text)  # 返回消息自动化编码 --不成功（有时候） == 80%
print(res_baidu.content.decode("utf8"))  # 指定编码方式 =20%

'''
https://www.baidu.com/s?wd=柠檬班
'''
url_bai2 = "https://www.baidu.com/s"
header_bai2 = {"User-Agent":
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"}
data_bai2 = {"wd":"柠檬班"}
res_baidu = requests.get(url=url_bai2,headers=header_bai2,params=data_bai2)
# print(res_baidu.text)  # 返回消息自动化编码 --不成功（有时候） == 80%
print(res_baidu.content.decode("utf8"))  # 指定编码方式 =20%