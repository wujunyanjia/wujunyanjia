"""
Project: 86python
Author:柠檬班-Tricy
Time:2021/11/29 18:55
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
"""
'''
1、在pycharm的控制台里输入以下内容，并且以如下格式输出到控制台

2、现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请取出并打印字符串中的'python'。[0:6] --切片
2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？-- in
3）替换python为 “lemon”. -- replace
4) 找到aaa的起始位置 -- 索引
'''
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")
# gender = input("请输入你的性别：")
# print('''********************
# 姓名：{}
# 年龄：{}
# 性别：{}
# ********************'''.format(name,age,gender))
#
# str1 = 'python hello aaa 123123aabb'
# print(str1[0:6:1])
# print("o a" in str1)
# print("he" in str1)
# print(str1.replace("python","lemon"))
# print(str1.find("aaa"))
# print(str1.index("aaa"))

'''
1：a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- if
2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。
3、list1 = ['Rella', '纯纯', '二丫', '小梨', '东东', '熊熊']
列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。--list2=[]
方法1： 手动扩充--字典--存放在列表里面；{} --简单
方法2： 自动--dict（）--不强制-- for循环 ，list2.append() --- 难度
4、for循环遍历其他的数据类型 --字典，列表 元组
'''
# a=[1,2,'6','summer']
# if "i" in a:
#     print("i是这个列表的成员！")
# else:
#     print("i不是列表的成员")
#
# dict_1={"class_id":45,'num':20}
# num = dict_1.get("num")
# if num > 5:
#     print("这个班级的人数是：{}".format(num))
# else:
#     print("班级人数不足5人！")

# 不唯一的
# dict1 = {"name":"Rella","gender":"male","age":18,"city":"深圳"}
# dict2 = {"name":"纯纯","gender":"male","age":18,"city":"深圳"}
# dict3 = {"name":"二丫","gender":"male","age":18,"city":"深圳"}
# dict4 = {"name":"小梨","gender":"male","age":18,"city":"深圳"}
# dict5 = {"name":"东东","gender":"male","age":18,"city":"深圳"}
# dict6 = {"name":"熊熊","gender":"male","age":18,"city":"深圳"}
# list2 = [dict1,dict2,dict3,dict4,dict5,dict6]
# print(list2)
# 不唯一
# list1 = ['Rella', '纯纯', '二丫', '小梨', '东东', '熊熊']
# list2 = [] #空列表
# for i in range(len(list1)):
#     dict1 = dict(name=list1[i],age=18,gender="male",city="北京")
#     list2.append(dict1)
# print(list2)

'''
1. 把字符串转成列表 - list()

2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和

3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if 判断嵌套 
'''
def judge_object(obj):
    if type(obj) == list or type(obj) == str  or  type(obj) == dict:
        if len(obj) > 5:
            print("True")
        else:
            print("False")
    else:
        print("数据类型错误！")

judge_object(12121)


# str1 = "hello world"
# list1 = list(str1)
# print(list1)
# 扩展： split() : 以某个字符分割字符串--得到结果是一个列表
# str1 = "http://13.2.3.4//"
# list2 = str1.split("//")
# print(list2)

# 方式一：
# sum1 = 0
# num1 = int(input("请输入一个任意的整数："))
# for i in range(num1):
#     sum1 += i
# print(sum1)
# 方式二：
# def add_fun(num):
#     sum2 = 0
#     for j in range(num):
#         sum2 += j
#     return sum2
#
# result = add_fun(100)
# print(result)


