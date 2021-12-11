"""
Project: 86python
Author:柠檬班-Tricy
Time:2021/12/3 19:01
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.
"""
'''
selenium : 工具  ==  实现UI自动化的
三个部分：
1、IDE  --  录制脚本 --少
2、webdriver -- 重要！！库 提供了对网页的操作的各种方法 == 针对不同的语言通用- python  java ，结合语言来使用
3、grid ： 分布式 -- 同时对对个浏览器并发执行  == 少

代码      --------驱动------    浏览器
python/java        中间人（浏览器驱动）            浏览器

三大等待方式：
1、time.sleep  == 强制等待

'''
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()   # 选择谷歌浏览器 建立一个会话  --赋值给一个变量
#
# # 打开网址 --百度
# # driver.get("https://www.baidu.com")
# # 最大化操作浏览器-窗口
# driver.maximize_window()
# # 前进 后退 和刷新操作
# driver.get("http://www.taobao.com")
# time.sleep(2)  # 代码等待2s   == 睡了2s
# driver.back()  # 推后
# time.sleep(2)
# driver.forward() # 前进
# time.sleep(2)
# driver.refresh()  # 刷新
# driver.close()  关闭浏览器

'''
UI自动化-- 主要的工作  定位元素 
认识网页页面  三个部分组成  --了解
1、HTML --标签语言 页面内容  <标签名>值</标签名> ==通过这个定位
2、CSS - 布局呈现 -- 字体颜色 大小 
3、JS -根据情况操作控制页面

元素 = 标签+ 属性  ： input - 输入框  div --块
属性：id  name  class  type  == 开发约定的，标准  --id 唯一 

元素定位的方法： 八大方式 ==  id name  xpath 
xpath定位：
绝对路径：从根开始 一级一级往下找 直到找到这个元素为止。 从/
/html/body/div/div/div[2]/div[3]/div/label[1]/div/ins == 根本不会xpath  公司用的很少
相对路径：// 开头 ，标签+属性

1、定位到这个元素  
2、对它进行操作

对元素四大操作：
1、输入操作  --send_keys
2、点击  -- click
3、获取文本--内容--text
4、获取属性值 -get_attribute

三大等待：
1、强制等待：time.sleep  ：简单，但是不够智能，就算元素已经出现了，时间没有到，还得继续等待 -- 影响代码执行的执行速度
2、智能等待： -隐式等待 ：只要元素出现了，不继续等了，直接开始执行后续的代码 == 一个会话只要写一次就可以
            --显性等待 -- 以后在自动化班级去学！！

UI自动化： 冒烟测试  -- 项目主流程跑通

经典的面试一：UI自动化查找元素的时候，浏览器里面xpath 唯一找到， 但是代码里报错 报错，请问原因有哪些？
1、 页面发生了切换  -- 等待
2、 id定位，变化的--报错
3、 页面里面存在子页面  要先进行子页面的切换

面试题二： 你有没有搭建自动化框架？-- 没有，框架有专门的自动化组搭建或者 原来公司就有，可以自己写自动化的脚本！
          有没有见过你们自动化框架的组成部分？ -- 介绍
          公共代码方法 -- common 包
          测试数据  ==  testdata-- Python文件定义好
          日志和报告机制  ==  test result  - report  log文件
          启动文件  -- run.py  -- 调用

'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()   # 选择谷歌浏览器 建立一个会话  --赋值给一个变量
driver.implicitly_wait(10)  # 隐式等待  --写一次够了

driver.get("http://erp.lemfix.com/login.html")
title = driver.title  # 可以获取页面的标题
if title == "柠檬ERP":
    print("页面的标题是：{}".format(title))
else:
    print("页面标题不对！")
# driver.find_element_by_id("username").send_keys("sunny")  # 找到元素 进行输入用户名
# driver.find_element_by_name("username").send_keys("sunny")
# driver.find_element_by_id("password").send_keys("123456")  # 找到元素 进行输入密码
# driver.find_element_by_id("btnSubmit").click() # 找到元素 进行点击
driver.find_element(By.ID,"username").send_keys("sunny")
driver.find_element(By.ID,'password').send_keys("123456")
driver.find_element(By.ID,"btnSubmit").click()

# 第四条用例： 判断是否登录成功  --  找下一下页面里元素  有没有 用户名存在？  == sunny
# time.sleep(2)  # 发生了页面切换 -等待
username = driver.find_element(By.XPATH,'//p').text  # 获取文本
if username == "sunny":
    print("登录成功")
else:
    print("登录失败")

# 第五条用例： 点击零售出库
driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
# 第六条用例： 搜索单据编号
'''
iframe页面操作： 当一个html页面里面嵌套了一个html页面  == 子页面的里的元素 先切换到子页面才可以！！
1、如何去 寻找 发现存在子页面？  -- 标签路径里 是否iframe 标签 --后面跟的子页面
2、如何切换iframe页面：
本质上也是一个元素   相当于元素的定位
1）id name  == iframe标签的里的id进行切换 
注意： id如果是变化的，那么不能使用来作为元素定位！！
2） webelement  -- 元素定位表达式 进行切换 --iframe

'''
id = driver.find_element(By.XPATH,'//div[text()="零售出库"]/..').get_attribute("id") # 获取ID属性
frame_id = id + '-frame'  # 得到iframe id

driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="{}"]'.format(frame_id)))  # 通过id进行 iframe的子页面的切换
driver.find_element(By.ID,"searchNumber").send_keys("566")  # 对子页面的元素进行操作了
driver.find_element(By.ID,'searchBtn').click()
time.sleep(0.1) # 强制等待辅助
text = driver.find_element(By.XPATH,'//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text # 获取值
if "566" in text:
    print("搜索结果正确！")
else:
    print("搜索错误")