"""
Project: 86python
Author:柠檬班-Tricy
Time:2021/11/26 20:05
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
"""
'''
控制流：循环--for循环  判断 --if语句
if 条件: # 这个条件满足的情况 成立  ==  冒号   ==断言
    分支执行语句   -- 分支语句  --子分支  ==缩进 ： 4个空格的缩进 - tab键
elif 条件：   --elif   可有 也可以没有  也可以有多个 
    分支执行语句
elif 条件：
     分支执行语句
else:  -- 兜底  没有条件
    执行分支语句
    
注意： input输入数据 统一都是字符串类型！！

money = int(input("请输入你的存款金额："))  # int()转化为整形
if money >= 200:  # 比较运算符 -- 布尔值 == True =1 False =0
    print("买个house！")
elif  200 > money >= 100:
    print("开个小卖部！")
elif money >= 50:
    print("买车")
elif money >= 10:
    print("买点家用品")
else:
    print("打工人打工魂！")
    
循环： for -- 多 ： 遍历 每一个元素 =for循环
循环次数  == 谁控制？== 元素个数
遍历各种数据类型： 字符串  元组  字典 （key value --key？value？）

扩展一个小工具： debug 工具 -- 代码调试工具
1、打断点  ==调试从这行开始运行
2、点击 debug 按钮  == 开始一行一行的运行
3、单步执行

扩展：中断循环
break == 中止循环 跳出所有的循环
continue  == 中断本次循环 跳出本次循环  后续的循环继续！
list1 = ['小米', 'Gala', 'sam', '小梅', '小太阳', '一凡', '小七', 'Z', '甜甜', '无我']
count = 0
for name in list1:
    if name == "一凡":
        # break
        continue
    print(name)
    print("***" * 10)
    count += 1
print(count)

内置函数: for结合一起使用  range  == 用来生成一个整数序列的函数  == 编号
star : 从star开始，不填可以省略 -= 默认从0
stop ： 不可以省略 
step： 可以  默认1
原则： 取头不取尾
for i in range(1,100):
    print(i)

函数：一些频繁使用到的功能 每次用到的时候  重新写一次代码  -- 麻烦 
      把这种需要重复使用的功能的代码 --封装 成 函数  == 调用就好 == 提高代码复用率
内置函数: pyton底层本来就写好的  可以直接拿来用！ print()  input()  int()  str()

怎么封装 语法：
def 函数名():  -- 标识符的命名规则？
    函数体 （子代码）== 具体函数实现的功能代码
注意： 函数不调用  不会运行的！！  定义了函数 没有调用   不会运行！

优化：
1、函数里面 不应该存在一些经常会变化的数据 ---  参数化  == 变成函数参数  --括号里
   定义的参数  --形参
   调用的函数的传入参数  -- 实参

参数定义方式：
1、必备参数： 定义了就必须要还要传的参数 -- 不传会报错
2、默认参数： 可以不给参数设置一个默认，调用的时候可以不传了！- 直接用默认值； 可以传参数，传入的为准！
注意: 默认参数 一定要放在必备参数的后面！
3、不定长参数： 不确定长度, 可以不传 多个 
*args: 等前面的必备参数和默认参数都接受完了之后，剩下的参数 都会被这个不定长参数接受！并且以元组的格式保存！-不必须放在最后
       位置传参的 多余的参数 == 接受
**kwargs:等前面的必备参数和默认参数都接受完了之后，剩下的参数都会被这个不定长参数接受！并且以字典的格式保存！-- 一定放最后的！
       关键字传参的 多余的参数 == 接受

参数传入的方式;
1、 位置传参： 严格按照位置顺序进行参数传入  -- 位置敏感
2、 关键字传参: 指定了形参的名字进行传参 --位置无所谓 == 精确
注意： 混合传参，对顺序有要求： 关键字传参的方式 一定要放在位置传参方式后面！！

遗留问题：
1、sum1 没有加到工作总和？？  == for循环

函数有进有出 ： 进 --参数， 出-- 返回值
函数返回值： return  = 当我使用这个函数时候，有一个或者多个需要从这个函数里获得的数据，用于后面的代码功能
           如果函数定义了返回值，调用函数的时候就可以使用变量接受返回值！
1、可以有，可以没有-- 返回的None ，可以有多个--定义的时候用逗号隔开，接受的时候- 元组保存的
2、返回值一定要写在最后  --return 后面就跳出函数体
   return后面的代码不会再执行了
注意： 函数的定义里面不会出现可能会变化的数据 -- 参数化
      打印的内容不会出现再函数里面！
def good_job(salary,bonus,subsidy=500,*args,**kwargs):
    sum1 = salary + bonus + subsidy
    for num in args:
        sum1 += num
    for i in kwargs:
        sum1 += kwargs.get(i)  #字典的取值 --key 取value
    print("salary参数值是: {}".format(salary))
    print("bonus参数值是: {}".format(bonus))
    print("subsidy参数值是: {}".format(subsidy))
    print("args参数值是: {}".format(args))
    print("kwargs参数值是: {}".format(kwargs))
    print("工资总和是：{}".format(sum1))
    return sum1,salary   # 定义函数的返回值
    print("这行代码你会执行么？")
'''
# def good_job(salary,bonus,subsidy=500,*args,**kwargs):
#     sum1 = salary + bonus + subsidy
#     for num in args:
#         sum1 += num
#     for i in kwargs:
#         sum1 += kwargs.get(i)  #字典的取值 --key 取value
#     return sum1,salary   # 定义函数的返回值
#
# sum = good_job(10000,1000,300,300,500,800,a=1000,b=200,c=300)  # 对函数的调用  --  函数名字调用！
# print("工资总和是：{}".format(sum))

# if sum > 12000:
#     print("这个是个不错的工作！")
# else:
#     print("考虑考虑")

'''
内置函数：
print
input
type ， isinstance
len
str  int float bool  list tuple dict set   ==数据类型
range
字符串的内置方法： index find count replace  format
列表的内置方法：append insert pop delete clear extend 
字典的内置方法： get() update pop 
'''
sum1 = 0
for i in range(1,10):
    sum1 += i
print(sum1)