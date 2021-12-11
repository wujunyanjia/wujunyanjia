"""
Project: 86python
Author:柠檬班-Tricy
Time:2021/11/22 20:53
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
"""
'''
标识符：凡是自己取的名字 -- 命名规则
1、只能包含数字 字母 和下划线   -- 变量  函数  类
2、不能以数字开头 
3、不能用关键字 : python 自己先定义好了  有自己特殊意义的字
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
4、建议：不同的数字和字母之间下划线隔开  python_class_86  ==方便阅读 == 驼峰命名  PythonClass
‘
运行Python脚本：
1、第一次+ 右键  run
2、控制台-- 运行
3、右上角 --选对文件  运行
4、 菜单栏 -- run  == 快捷键  

print（） ---  内置函数：Python预先定义好的 可以直接使用的功能 ：打印内容到控制台

注释：
Python里注释几种方式：
1、单行注释： # 后面的内容 就会被注释掉
2、快捷注释方式 ：ctrl + /  取消注释
3、多行注释 ： 三引号 '''  ''' , """ """
为什么需要注释：== 不写注释的代码员，不是好代码员
1、给别人看  == 解释说明
2、给自己看  
3、功能被删掉  == 注释掉了 

基本格式要求
1、所有的代码 （除非父子关系） -- 顶格编写  == 函数  循环 控制流 
2、大小写敏感的 

常用数据类型：
1、整型 - int
内置函数：判断数据类型：
type(): 判断数据的类型，返回结果类型
isinstance(20,float): 判断类型，结果-布尔值
2、浮点型：float
3、布尔值  --真 和假 == True  False
4、字符串 - str：  用成对的引号括起来的内容   = 单引号，双引号 ，三引号
1) 引号的嵌套  -- UI自动化测试
2） 三引号 可以保持格式  == 所见即所得

'''
# print('甜甜是86期的班花!')
# print('一凡是86期的班草!')
print('86的"小米"'
      '是'
      '富'
      '婆!')
print('''---Gala的基本信息---
名字：gala
    性别：男
        爱好：女
''')
print(20)
print(type(20.34))
print(isinstance(20,float))

'''
变量：存储数据的容器  == 简化代码维护  == 名字是自己取的么？-- 标识符的命名规则呢？
1、只能包含数字 字母 和下划线   -- 变量  函数  类
2、不能以数字开头 
3、不能用关键字 : python 自己先定义好了  有自己特殊意义的字
4、变量名字一定要先定义（申明）再调用

字符串常用操作：
1、字符串取值：每一个元素都有自己位置 -- 编号 == 索引 ==从0开始，一次编号  ==通过索引来取值
2、取多个值 == 切片 =  起始位置 start    终止位置 stop    步长 
注意： 取头不取尾 == 夺取一步 
3、字符串的长度  - len() ==元素个数
'''
str1 ='''hello lemon86'''   # 定义了一个字符串  --赋值给了一个变量
#        0123456789101112
print(str1[11]) # 通过索引取值
print(str1[-1]) # -1 最后一个元素
print(str1[-2]) # -1 最后一个元素
print(str1[0]) # -1 最后一个元素
print(str1[6:13:1])
print(len(str1))









